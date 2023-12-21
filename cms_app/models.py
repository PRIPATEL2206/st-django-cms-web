import os
from typing import Any
from django.db import models
from django.contrib.auth.models import User

def upload_path(instance,filename) -> str:
    return os.path.join('image/',filename)

class CMSUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(default="")
    role=models.CharField(default="Customer",max_length=30)
    role_ID=models.PositiveSmallIntegerField(default=1,)
    contect_number=models.CharField(max_length=20)
    balance=models.BigIntegerField(default=10000)
    profile_img=models.ImageField(upload_to=upload_path,null=True)



class Product(models.Model):
    # pID=models.AutoField(auto_created=True,unique=True)
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to=upload_path,null=True)
    prize=models.PositiveIntegerField(default=0)
    discription=models.TextField(default="")
    quntity=models.PositiveSmallIntegerField(default=0)
    added_datetime=models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    # cart_ID=models.AutoField(auto_created=True,unique=True)
    owner=models.ForeignKey(CMSUser,on_delete=models.DO_NOTHING)
    products: list[type[Product]]=[]
    is_buyed=models.BooleanField(default=False)
    cart_making_date=models.DateTimeField(auto_now_add=True)
    buying_date=models.DateTimeField(null=True)
    total_prize=models.PositiveIntegerField(default=0)

    def add_product(self,product:Product):
        self.products.append(product)
        self.total_prize+=product.prize

    def delete_product(self,product:Product):
        self.products.remove(product)
        self.total_prize-=product.prize
    
class Order(models.Model):
    # order_id=models.AutoField(auto_created=True,unique=True)
    buyer=models.ForeignKey(CMSUser,related_name="Customer",on_delete=models.DO_NOTHING)
    validator_employee=models.ForeignKey(CMSUser,related_name="validatore",on_delete=models.DO_NOTHING)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    total_prize=models.PositiveIntegerField(default=0)
    address=models.TextField(default="")
    status=models.CharField(max_length=100)
    status_code=models.PositiveSmallIntegerField(default=0)
    discription=models.TextField(default="") #customer remark
    remark=models.TextField(default="") #employee remark


