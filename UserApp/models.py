from django.db import models
from AdminApp.models import*


class Register (models.Model):
    username=models.TextField(max_length=50)
    phonenumber=models.IntegerField()
    email=models.EmailField(default=0)
    password=models.CharField(max_length=123)

class Cart (models.Model):
    user_id=models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    productquantity=models.IntegerField(default=1)
    totalamount = models.IntegerField(default=0)

class checkout(models.Model):
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=234,default=0)
    city = models.CharField(max_length=244,default=0)
    pincode = models.IntegerField(default=0)
    country = models.CharField(max_length=25,default=0)

    

    
    
    


# Create your models here.
