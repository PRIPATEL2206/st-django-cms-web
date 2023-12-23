from email.policy import default
import os
from typing import Any
from uuid import uuid1
from django.db import models
from django.contrib.auth.models import User

ROLES={
    1:"customer",
    2:"employee",
    3:"master"
}

BASE_BALANCE=10000

def upload_user_path(instance,filename) -> str:
    print(instance)
    return os.path.join('user_images/',uuid1().hex+filename)

def upload_product_path(instance,filename) -> str:
    return os.path.join('product_images/',uuid1().hex+filename)

class CMSUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    address=models.TextField(default="")
    role=models.CharField(default="Customer",max_length=30)
    role_ID=models.PositiveSmallIntegerField(default=1,)
    contect_number=models.CharField(max_length=20)
    balance=models.BigIntegerField(default=BASE_BALANCE)
    profile_img=models.ImageField(upload_to=upload_user_path,null=True)



class Cart(models.Model):
    # cart_ID=models.AutoField(auto_created=True,unique=True)
    owner=models.ForeignKey(CMSUser,on_delete=models.CASCADE)
    # products: list[type[Product]]=[]
    is_buyed=models.BooleanField(default=False)
    cart_making_date=models.DateTimeField(auto_now_add=True)
    buying_date=models.DateTimeField(null=True,default=None)
    total_prize=models.PositiveIntegerField(default=0)

    # def add_product(self,product:Product):
    #     self.products.append(product)
    #     self.total_prize+=product.prize
    #     self.save()

    # def delete_product(self,product:Product):
    #     self.products.remove(product)
    #     self.total_prize-=product.prize
    #     self.save()
    
class Product(models.Model):
    # pID=models.AutoField(auto_created=True,unique=True)
    name=models.CharField(max_length=100)
    isCopy=models.BooleanField()
    img=models.ImageField(upload_to=upload_product_path,null=True)
    prize=models.PositiveIntegerField(default=0)
    discription=models.TextField(default="")
    quntity=models.PositiveSmallIntegerField(default=0)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,default=None,null=True)
    added_datetime=models.DateTimeField(auto_now_add=True)


    
class Order(models.Model):
    # order_id=models.AutoField(auto_created=True,unique=True)
    buyer=models.ForeignKey(CMSUser,related_name="Customer",on_delete=models.CASCADE)
    validator_employee=models.ForeignKey(CMSUser,related_name="validatore",on_delete=models.DO_NOTHING)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    total_prize=models.PositiveIntegerField(default=0)
    address=models.TextField(default="")
    status=models.CharField(max_length=100)
    status_code=models.PositiveSmallIntegerField(default=0)
    discription=models.TextField(default="") #customer remark
    remark=models.TextField(default="") #employee remark


