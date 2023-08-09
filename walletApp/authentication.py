from rest_framework.authentication import TokenAuthentication
from walletApp.models import Customer

class Authentication(TokenAuthentication):
    def authenticate(self, request):
        key = request.META.get('HTTP_AUTHORIZATION')

        if not key:
            return None
        key = key[6:]
        try:
            ua = Customer.objects.get(key=key)
        except Customer.DoesNotExist:
            return None

        return (ua,None)
