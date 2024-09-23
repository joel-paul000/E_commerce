from django.db import models

class Category(models.Model):
    cateogoryname=models.TextField(max_length=50)


class Product(models.Model):
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    productname=models.TextField(max_length=50)
    productquantity=models.IntegerField(default=0)
    productprice=models.IntegerField(default=0)
    productimage=models.ImageField(upload_to="proimage",default="null.jpg")



# Create your models here.
