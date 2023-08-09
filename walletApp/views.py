from walletApp.models import Customer, Wallet, Transactions
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from walletApp.authentication import Authentication
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
import uuid

# Create your views here.

class InitializeWallet(APIView):
    def post(self,request):
        customer_xid = request.POST.get('customer_xid')
        customer = Customer.objects.filter(id=customer_xid).first()
        if not customer:
            return JsonResponse({
                "status":"fail",
                "data":{
                    "error" : "Could not find the given customer"
                }
            })
        token,_ = Token.objects.get_or_create(user=customer)

        customer.key = token.key
        customer.save()

        data = {'token':token.key}

        return JsonResponse({"status":"success","data":data})


class EnableWallet(APIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        key = request.META.get('HTTP_AUTHORIZATION')[6:]
        customer = Customer.objects.filter(key = key).first()
        wallet = Wallet.objects.filter(customer=customer).first()

        if wallet is not None and wallet.status == 'enabled':
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Already enabled"
                }
            })

        if not wallet:
            wallet = Wallet(
                id=str(uuid.uuid4()),
                customer = customer,
                status = "enabled",
                balance = 0,
                enabled_at = timezone.now()
            )
        else:
            wallet.status = "enabled"
            wallet.enabled_at = timezone.now()
        
        wallet.save()

        data = {
            "wallet" : {
                "id" : wallet.id,
                "owned_by" : wallet.customer.id,
                "status" : wallet.status,
                "enabled_at" : wallet.enabled_at,
                "balance" : wallet.balance
            }
        }
    
        return JsonResponse({"status":"success","data":data})
    
    def get(self,request):
        key = request.META.get('HTTP_AUTHORIZATION')[6:]
        customer = Customer.objects.filter(key = key).first()
        wallet = Wallet.objects.filter(customer=customer).first()

        if wallet is not None and wallet.status != "enabled":
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Wallet disabled"
                }
            })

        if not wallet:
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Could not find wallet"   
                }
            })
        else:
            data = {
                "wallet" : {
                    "id" : wallet.id,
                    "owned_by" : wallet.customer.id,
                    "status" : wallet.status,
                    "enabled_at" : wallet.enabled_at,
                    "balance" : wallet.balance
                }
            }
    
        return JsonResponse({"status":"success","data":data})
    
    def patch(self,request):
        key = request.META.get('HTTP_AUTHORIZATION')[6:]
        is_disabled = request.POST.get("is_disabled")

        if not is_disabled:
            return
        
        customer = Customer.objects.filter(key = key).first()
        wallet = Wallet.objects.filter(customer=customer).first()

        if not wallet:
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Could not find wallet"   
                }
            })

        wallet.status = "disabled"
        wallet.disabled_at = timezone.now()
        wallet.save()

        data = {
            "wallet" : {
                    "id" : wallet.id,
                    "owned_by" : wallet.customer.id,
                    "status" : wallet.status,
                    "disabled_at" : wallet.disabled_at,
                    "balance" : wallet.balance
            }
        }

        return JsonResponse({"status":"success","data":data})
    

class WalletTransaction(viewsets.ViewSet):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    
    @action(methods=['GET'],detail=False)
    def transactions(self,request):
        key = request.META.get('HTTP_AUTHORIZATION')[6:]

        customer = Customer.objects.filter(key = key).first()
        transactions = Transactions.objects.filter(customer=customer).values()

        data = {"transactions":[]}

        for t in transactions:
            data["transactions"].append(
                {
                    "id" : t['id'],
                    "status" : t["status"],
                    "transacted_at" : t["transacted_at"],
                    "type" : t["type"],
                    "amount" : t["amount"],
                    "reference_id" : t["reference_id"]
                }
            )

        return JsonResponse({"status":"success","data":data})
    
    @action(methods=['POST'],detail=False)
    def deposits(self,request):
        key = request.META.get('HTTP_AUTHORIZATION')[6:]

        customer = Customer.objects.filter(key = key).first()
        wallet = Wallet.objects.filter(customer=customer).first()

        if not wallet:
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Could not find wallet"   
                }
            })

        if wallet.status != "enabled":
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Wallet disabled"
                }
            })

        amount = int(request.POST.get("amount"))
        reference_id = request.POST.get("reference_id")

        existing_transaction = Transactions.objects.filter(reference_id=reference_id).first()
        if existing_transaction is not None and reference_id == existing_transaction.reference_id:
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Transaction reference_id already exists"
                }
            })

        wallet.balance = wallet.balance + amount
        wallet.save()
        transaction = Transactions(
            id = str(uuid.uuid4()),
            reference_id = reference_id,
            customer = customer,
            type = "deposit",
            status = "success",
            amount = amount,
            transacted_at = timezone.now()
        )

        transaction.save()
        data = {
            "deposit" : {
                "id" : transaction.id,
                "deposited_by" : transaction.customer.id,
                "status":transaction.status,
                "deposited_at":transaction.transacted_at,
                "amount":transaction.amount,
                "reference_id":transaction.reference_id
            }
        }

        return JsonResponse({"status":"success","data":data})
    

    @action(methods=['POST'],detail=False)
    def withdrawals(self,request):
        key = request.META.get('HTTP_AUTHORIZATION')[6:]

        customer = Customer.objects.filter(key = key).first()
        wallet = Wallet.objects.filter(customer=customer).first()

        if not wallet:
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Could not find wallet"   
                }
            })

        if wallet.status != "enabled":
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Wallet disabled"
                }
            })

        amount = int(request.POST.get("amount"))
        reference_id = request.POST.get("reference_id")

        existing_transaction = Transactions.objects.filter(reference_id=reference_id).first()
        if existing_transaction is not None and reference_id == existing_transaction.reference_id:
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Transaction reference_id already exists"
                }
            })
        
        transaction = Transactions(
            id = str(uuid.uuid4()),
            reference_id = reference_id,
            customer = customer,
            type = "deposit",
            status = "success",
            amount = amount,
            transacted_at = timezone.now()
        )
        
        if wallet.balance < amount:
            transaction.status = "fail"
            transaction.save()
            return JsonResponse({
                "status" : "fail",
                "data" : {
                    "error" : "Wallet balance is less than amount"
                }
            })

        wallet.balance = wallet.balance - amount
        wallet.save()
        transaction.save()
        data = {
            "withdrawal" : {
                "id" : transaction.id,
                "withdrawn_by" : transaction.customer.id,
                "status":transaction.status,
                "withdrawn_at":transaction.transacted_at,
                "amount":transaction.amount,
                "reference_id":transaction.reference_id
            }
        }

        return JsonResponse({"status":"success","data":data})