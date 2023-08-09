from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class Customer(AbstractUser):
    id = models.CharField(primary_key=True,max_length=120)
    username = models.CharField(unique=False,max_length=50,null=True)
    key = models.CharField(max_length=300,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    del_flg = models.BooleanField(default=False,null=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    def save(self,*args,**kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Customer,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return super().__str__()
    
    @property
    def is_authenticated(self):
        return True


class Wallet(models.Model):
    id = models.CharField(primary_key=True,max_length=120)
    customer = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,null=True)
    balance = models.IntegerField(null=True)
    enabled_at = models.DateTimeField(null=True)
    disabled_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    del_flg = models.BooleanField(default=False,null=True)

    def save(self,*args,**kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Wallet,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return super().__str__()

class Transactions(models.Model):
    id = models.CharField(primary_key=True,max_length=120)
    reference_id = models.CharField(max_length=120)
    customer = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    amount = models.IntegerField(null=True)
    transacted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    del_flg = models.BooleanField(default=False,null=True)

    def save(self,*args,**kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Transactions,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return super().__str__()