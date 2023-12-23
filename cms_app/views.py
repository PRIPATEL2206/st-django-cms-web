from datetime import datetime
import random
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cms_app.models import CMSUser, Cart, Order, Product
from cms_app.models import ROLES

@login_required(login_url="/login",redirect_field_name="home")
def index(request:HttpRequest):
    products=Product.objects.filter(isCopy=False),
    numberOfProductPerPage=12

    context={
        "pages":products[i:i+numberOfProductPerPage] for i in range(0,len(products),numberOfProductPerPage)
    }
    print("length of pages = ",len(context["pages"]))
    print("length of pages = ",len(context["pages"][0]))
    # print(context["pages"][0][0])
    return render(request=request,template_name="index.html",context=context)

@login_required(login_url="/login",redirect_field_name="home")
def userPage(request:HttpRequest,u_id):
    context={
        "user":CMSUser.objects.get(id=u_id)
    }
    return render(request=request,template_name="user.html",context=context)

@login_required(login_url="/login",redirect_field_name="home")
def allUsersPage(request:HttpRequest):
    users=CMSUser.objects.all()

    context={
        "pages":[users[i:i+12] for i in range(0,len(users),12)]
    }
    return render(request=request,template_name='allUsers.html',context=context)

@login_required(login_url="/login",redirect_field_name="home")
def addEmployee(request:HttpRequest):
    if request.POST:
        post=request.POST
        userName=post.get("name")
        password=post.get("password")
        User.objects.create_user(
            username=userName,email=post.get("Email"),password=password
        )
        user= auth.authenticate(
             request= request,username=userName,
             password=password
             )
        auth.login(request=request,user=user)
        print(userName)
        cms_user=CMSUser(
            user=user,
            address=post.get("Address"),
            role=ROLES[2],
            role_ID=2,
            contect_number=post.get("phone"),
            profile_img=request.FILES.get("img"),
            email=post.get("Email")
        )
        cms_user.save()
        
    return render(request=request,template_name="addEmployee.html")

@login_required(login_url="/login",redirect_field_name="cart")
def buyCart(request:HttpRequest,c_id):
    cart=Cart.objects.get(id=c_id)
    if cart.owner.user.username==request.user.username and cart.owner.balance>=cart.total_prize:
        cart.is_buyed=True
        cart.buying_date=datetime.now()
        cart.owner.balance-=cart.total_prize
        cart.owner.save()
        cart.save()

        order=Order(
            buyer=cart.owner,
            validator_employee=random.choice(CMSUser.objects.filter(role_ID=2)),
            cart=cart,
            total_prize=cart.total_prize,
            address=cart.owner.address,
            status="Waiting to aprove",
            status_code=0,
            discription="",
            remark=""
        )
        order.save()

    return redirect('/cart')

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def aproveOrder(request:HttpRequest,o_id):
    print("aprove")
    order=Order.objects.get(id=o_id)
    order.status="Aproved"
    order.status_code=1
    order.save()
    return redirect("/ordersToAprove")

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def discardOrder(request:HttpRequest,o_id):
    order=Order.objects.get(id=o_id)
    order.status="Discarded"
    order.status_code=3
    order.save()
    return redirect("/ordersToAprove")

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def orderAprovePage(request:HttpRequest,o_id):
    order=Order.objects.get(id=o_id)
    context={
        "order":order,
        "products":Product.objects.filter(cart=order.cart,isCopy=True),
    }
    print(context)
    return render(request=request,template_name="orderAprovePage.html",context=context)

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def ordersToAprove(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    orders=Order.objects.filter(validator_employee=cmsUser,status_code=0)
    context={
        "orders":[
            {"order":order,"porducts":Product.objects.filter(cart=order.cart)}for order in orders
        ],
    }
    return render(request=request,template_name="orderAprove.html",context=context)

@login_required(login_url="/login",redirect_field_name="cart")
def myOrders(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    orders=Order.objects.filter(buyer=cmsUser)
    context={
        "orders":[{"order":order,"products":Product.objects.filter(cart=order.cart)} for order in orders]
    }

    print(len(context["orders"]))
    return render(request=request,template_name="myOrder.html",context=context)

@login_required(login_url="/login",redirect_field_name="home")
def removeFromCart(request:HttpRequest,p_id):
    pro=Product.objects.get(id=p_id,isCopy=True)
    pro.cart.total_prize-=pro.prize*pro.quntity
    pro.cart.save()
    pro.delete()
    print(pro)
    return redirect("/cart")

@login_required(login_url="/login",redirect_field_name="cart")
def incrementProductQuntity(request:HttpRequest,p_id):
    product=Product.objects.get(id=p_id)
    product.quntity+=1
    product.save()
    product.cart.total_prize+=product.prize
    product.cart.save()
    return redirect("/cart")

@login_required(login_url="/login",redirect_field_name="cart")
def dicrementProductQuntity(request:HttpRequest,p_id):
    product=Product.objects.get(id=p_id)
    if product.quntity!=0:
        product.cart.total_prize-=product.prize
        product.cart.save()
        
    product.quntity=max(product.quntity-1,0)
    product.save()
    return redirect("/cart")

@login_required(login_url="/login",redirect_field_name="cart")
def cartPage(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    userCart=Cart.objects.filter(owner=cmsUser,is_buyed=False)
    if not userCart:
        userCart=Cart(owner=cmsUser)
    else:
        userCart=userCart[0]
    context={
        "cart":userCart,
        "products":Product.objects.filter(cart=userCart,isCopy=True)
    }
    # print(context)
    return render(request=request,template_name="cart.html",context=context)

@login_required(login_url="/login",redirect_field_name="home")
def addToCart(request:HttpRequest,p_id):
    
    cmsUser=CMSUser.objects.get(user=request.user)
    userCart=Cart.objects.filter(owner=cmsUser,is_buyed=False)
    product=Product.objects.get(id=p_id,isCopy=False)
    if not userCart:
        userCart=Cart(owner=cmsUser)
    else:
        userCart=userCart[0]
    userCart.total_prize+=product.prize
    userCart.save()
    userCartProduct=Product(
        name=product.name,
        isCopy=True,
        img=product.img,
        prize=product.prize,
        discription=product.discription,
        quntity=1,
        cart=userCart,
    )
    userCartProduct.save()
    print(userCart)
    return redirect('/')

@login_required(login_url="/login",redirect_field_name="addProduct")
def addProductPage(request:HttpRequest):
    if request.POST:
        try:
            post=request.POST
            cms_product=Product(
                name=post.get("name"),
                img=request.FILES.get("img"),
                prize=post.get("price"),
                discription=post.get("desc"),
                isCopy=False,
            )
            print(cms_product.name)
            cms_product.save()
        except Exception as e:
            print(e)

    return render(request=request,template_name="addProduct.html")

@login_required(login_url="/login",redirect_field_name="profile")
def updateProfile(request:HttpRequest):
    try:
        if request.POST:
            post=request.POST
            print(post)
            user=User.objects.get(username=post.get("name"))
            if user.username!=request.user.username:
                print("not have asses")
                return redirect("/profile")

            cmsUser=CMSUser.objects.get(user=user)
            cmsUser.user.email=post.get("Email")
            cmsUser.email=post.get("Email")
            cmsUser.address=post.get("Address")
            cmsUser.profile_img=request.FILES.get("img") if request.FILES.get("img") else cmsUser.profile_img
            cmsUser.contect_number=post.get("phone")
            cmsUser.user.save()
            cmsUser.save()

    except Exception as e:
        print(e)

    return redirect("/profile")

@login_required(redirect_field_name="profile",login_url="/login")
def profile(request:HttpRequest):
    user=request.user
    cmsUser=CMSUser.objects.get(user=user)
    print(cmsUser.user.username)
    context={
        "userName":cmsUser.user.username,
        "email":cmsUser.user.email,
        "userName":cmsUser.user.username,
        "role":cmsUser.role,
        "roleId":cmsUser.role_ID,
        "address":cmsUser.address,
        "contect":cmsUser.contect_number,
        "balance":cmsUser.balance,
        "image":cmsUser.profile_img.url if cmsUser.profile_img else None
    }
    return render(request=request,template_name="profile.html",context=context)

def login(request:HttpRequest):
    context={}
    if request.POST:
        try:
            print(request.POST)
            email=request.POST.get('email')
            password=request.POST.get('password')
            username=CMSUser.objects.get(email=email).user.username
            user= auth.authenticate(request=request, username=username,password=password)
            
            if user:
                auth.login(request=request,user=user)
                return redirect("/")
            context["massage"]="Fail to login user user not found "

        except Exception as e:
            print(e)
            context["massage"]="Fail to login user"
    print(context)
    return render(request,"login.html",context=context)

def register(request:HttpRequest):
    context={}
    if request.POST:
        password=request.POST.get('pwd')
        password2=request.POST.get('cpwd')
        
        if password2==password:
            try:
                user_name=request.POST.get('name')
                print(user_name)
                email=request.POST.get('Email')
                address=request.POST.get('Address')
                phone=request.POST.get("phone")
                photo=request.FILES.get("img")


                User.objects.create_user(username=user_name,email=email,password=password)
                user= auth.authenticate( request= request,username=user_name,password=password)
                auth.login(request=request,user=user)
                print(email)
                cms_user=CMSUser(
                    user=user,
                    address=address,
                    role=ROLES[1],
                    role_ID=1,
                    contect_number=phone,
                    profile_img=photo,
                    email=email
                )
                cms_user.save()

                return redirect("/")
            except Exception as e :
                print(e.args)
                context["massage"]="Fail to create user"
    print(context)
                
    return render(request,"register.html",context=context)