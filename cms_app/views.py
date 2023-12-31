from datetime import datetime
import random
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from cms_app.models import CMSUser, Cart, Order, Product
from cms_app.models import ROLES
from .utils import send_email_to_users

@login_required(login_url="/login",redirect_field_name="home")
def index(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    products=Product.objects.filter(isCopy=False),
    numberOfProductPerPage=12

    context={
        "pages":products[i:i+numberOfProductPerPage] for i in range(0,len(products),numberOfProductPerPage)
    }
    context["roleId"]=cmsUser.role_ID
    return render(request=request,template_name="index.html",context=context)

@login_required(login_url="/login",redirect_field_name="admin")
def dashBord(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID != 3:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    monthTextMap={
        1:"Jan",
        2:"Fab",
        3:"Mar",
        4:"Apr",
        5:"May",
        6:"Jun",
        7:"Jul",
    8:"Aug",
        9:"Sep",
        10:"Oct",
        11:"Nav",
        12:"Dec",
    }
    monthList= list(range(1,13))

    #today date
    todayDate=datetime.now()

    #productwise salse
    unicProucts=Product.objects.filter(isCopy=False)
    itemWiseSalse={
        "lable":[pro.name for pro in unicProucts],
        "data":[sum([(pro.prize*pro.quntity) for pro in Product.objects.filter(isCopy=True,name=uPro.name) if pro.cart and pro.cart.is_buyed]) for uPro in unicProucts],
    }
    # customer wise selse

    customers=CMSUser.objects.all()
    customerWiseSalse={
        "lable":[customer.user.username for customer in customers],
        "data":[sum([cart.total_prize for cart in Cart.objects.filter(owner=cmsUser,is_buyed=True)]) for cmsUser in customers]
    }

    #yearly salse
    year_wise_salse=[sum([cart.total_prize for cart in Cart.objects.filter(is_buyed=True) if cart.buying_date.year==year]) for year in range(todayDate.year-9,todayDate.year+1)]
    yearlySalse={
        "lable":[i for i in range(todayDate.year-9,todayDate.year+1)],
        "data":year_wise_salse,
        "total":sum(year_wise_salse),
        "avarage_daily_salse":round(sum(year_wise_salse)/(10*12*30))
    }

    #monthly salse
    months=monthList[:todayDate.month]
    month_wise_salse=[sum([cart.total_prize for cart in Cart.objects.filter(is_buyed=True) if cart.buying_date.year==todayDate.year and cart.buying_date.month==month  ]) for month in months]
    monthlySalse={
        "lable":[ monthTextMap[i] for i in months],
        "data":month_wise_salse,
        "total":sum(month_wise_salse)
    }

    context={
        "roleId":cmsUser.role_ID,
        "dateTime":todayDate,
        "itemWiseSalse":itemWiseSalse,
        "customerWiseSalse":customerWiseSalse,
        "yearlySalse":yearlySalse,
        "monthlySalse":monthlySalse
    }
        
    return render(request=request,template_name="dashBord.html",context=context)

@login_required(login_url="/login",redirect_field_name="home")
def userPage(request:HttpRequest,u_id):
    cmsUser=CMSUser.objects.get(id=u_id)
    if CMSUser.objects.get(user=request.user).role_ID != 3:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")

    context={
        "user":cmsUser,
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
    }
    return render(request=request,template_name="user.html",context=context)

@login_required(login_url="/login",redirect_field_name="home")
def allUsersPage(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID !=3:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    users=CMSUser.objects.all()
    context={
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
        "pages":[users[i:i+12] for i in range(0,len(users),12)]
    }
    return render(request=request,template_name='allUsers.html',context=context)

@login_required(login_url="/login",redirect_field_name="home")
def addEmployee(request:HttpRequest):
    reqCmsUser=CMSUser.objects.get(user=request.user)
    if reqCmsUser.role_ID !=3:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    if request.POST:
        post=request.POST
        userName=post.get("name")
        password=post.get("password")
        user=User.objects.create_user(
            username=userName,email=post.get("Email"),password=password
        )
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
        messages.success(request=request, message=str(user.username)+" added sucsessfully")
    context={
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
    }
        
    return render(request=request,template_name="addEmployee.html",context=context)

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
        messages.success(request=request, message="place order sucsessfully")
        send_email_to_users(
            subject="Order Place Sucsessfuly",
            massage=f"your order is plased sucsessfuly \nyour order id is \" {order.id} \" \nOrder will be sheeped to address {order.address} \nCurent status : {order.status} \nTotal Prize : {order.total_prize} \n\n\n please fill free to contect us on {order.validator_employee.contect_number} ",
            to=[order.buyer.email]
        )
        send_email_to_users(
            subject="New order is comes",
            massage=f"New order is comes with order id \" {order.id} \" check it out to your account \ncustomer contect number : {order.buyer.contect_number}",
            to=[order.validator_employee.email]
        )
    else:
        messages.error(request=request, message="you not have acsses to this page ")

    context={
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
    }
    return redirect('/cart',context=context)

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def aproveOrder(request:HttpRequest,o_id):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID!=2:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    order=Order.objects.get(id=o_id)
    order.status="Aproved"
    order.status_code=1
    order.save()
    messages.success(request=request, message="Order aproveed sucsessfully")

    return redirect("/ordersToAprove/"+str(o_id))

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def shiping(request:HttpRequest,o_id):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID!=2:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    order=Order.objects.get(id=o_id)
    if order.status_code == 1:
        order.status="shiped to delivery"
        order.status_code=2
        order.save()
        messages.success(request=request, message="Order gose for shiping sucsessfully")
    return redirect("/ordersToAprove/"+str(o_id))

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def delivered(request:HttpRequest,o_id):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID!=2:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    order=Order.objects.get(id=o_id)
    if order.status_code == 2:
        order.status="delivered"
        order.status_code=10
        order.save()
        messages.success(request=request, message="Order delivered sucsessfully")
    return redirect("/ordersToAprove/"+str(o_id))

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def discardOrder(request:HttpRequest,o_id):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID!=2:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    order=Order.objects.get(id=o_id)
    order.status="Discarded"
    order.status_code=3
    order.buyer.balance+=order.total_prize
    order.buyer.save()
    order.save()
    messages.success(request=request, message="Order discarded sucsessfully")

    return redirect("/ordersToAprove")

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def orderAprovePage(request:HttpRequest,o_id):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID!=2:
        messages.error(request=request, message="you not have acsses to this page ")
        return redirect("/")
    order=Order.objects.get(id=o_id)
    context={
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
        "order":order,
        "products":Product.objects.filter(cart=order.cart,isCopy=True),
    }
    return render(request=request,template_name="orderAprovePage.html",context=context)

@login_required(login_url="/login",redirect_field_name="OrderToAprove")
def ordersToAprove(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID!=2:
        return redirect("/")
    cmsUser=CMSUser.objects.get(user=request.user)
    orders=[order for order in Order.objects.filter(validator_employee=cmsUser) if order.status_code not in [3,10]]
    context={
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
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
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
        "orders":[{"order":order,"products":Product.objects.filter(cart=order.cart)} for order in orders][::-1]
    }
    return render(request=request,template_name="myOrder.html",context=context)

@login_required(login_url="/login",redirect_field_name="home")
def removeFromCart(request:HttpRequest,p_id):
    pro=Product.objects.get(id=p_id,isCopy=True)
    if request.user.username!=pro.cart.owner.user.username:
        messages.error(request=request, message="you are not owner of this product")
        return redirect("/")
    pro.cart.total_prize-=pro.prize*pro.quntity
    pro.cart.save()
    pro.delete()
    messages.success(request=request, message=str(pro.name)+" remove from cart sucsessfully")
    return redirect("/cart")

@login_required(login_url="/login",redirect_field_name="cart")
def incrementProductQuntity(request:HttpRequest,p_id):
    product=Product.objects.get(id=p_id)
    if request.user.username!=product.cart.owner.user.username:
        messages.error(request=request, message="you are not owner of this product")
        return redirect("/")
    product.quntity+=1
    product.save()
    product.cart.total_prize+=product.prize
    product.cart.save()
    return redirect("/cart")

@login_required(login_url="/login",redirect_field_name="cart")
def dicrementProductQuntity(request:HttpRequest,p_id):
    product=Product.objects.get(id=p_id)
    if request.user.username!=product.cart.owner.user.username:
        messages.error(request=request, message="you are not owner of this product")
        return redirect("/")
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
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
        "cart":userCart,
        "products":Product.objects.filter(cart=userCart,isCopy=True)[::-1]
    }
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
    messages.success(request=request, message=str(product.name)+" added to cart sucsessfully")
    return redirect('/')

@login_required(login_url="/login",redirect_field_name="addProduct")
def addProductPage(request:HttpRequest):
    cmsUser=CMSUser.objects.get(user=request.user)
    if cmsUser.role_ID !=3:
        messages.error(request=request, message="You not have acsess to this page")
        return redirect("/")
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
            cms_product.save()
            messages.success(request=request, message="Product added sucsessfully")

        except Exception as e:
            messages.error(request=request, message="error while adding product "+ str(e.args))
    context={
        "roleId":CMSUser.objects.get(user=request.user).role_ID,
    }
    return render(request=request,template_name="addProduct.html",context=context)

@login_required(login_url="/login",redirect_field_name="profile")
def updateProfile(request:HttpRequest):
    try:
        if request.POST:
            post=request.POST
            user=User.objects.get(username=post.get("name"))
            if user.username!=request.user.username:
                messages.error(request=request, message="you not have acsses to this page ")
                return redirect("/profile")

            cmsUser=CMSUser.objects.get(user=user)
            cmsUser.user.email=post.get("Email")
            cmsUser.email=post.get("Email")
            cmsUser.address=post.get("Address")
            cmsUser.profile_img=request.FILES.get("img") if request.FILES.get("img") else cmsUser.profile_img
            cmsUser.contect_number=post.get("phone")
            cmsUser.user.save()
            cmsUser.save()
            messages.success(request=request, message="Profile updateted Sucsessfully")



    except Exception as e:
        messages.error(request=request, message="error wile updateting profile "+str(e.args))
    return redirect("/profile")

@login_required(redirect_field_name="profile",login_url="/login")
def profile(request:HttpRequest):
    user=request.user
    cmsUser=CMSUser.objects.get(user=user)
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

@login_required(login_url="/login",redirect_field_name="logout")
def logout(request:HttpRequest):
    auth.logout(request=request)
    messages.success(request=request, message="You have Logout sucsessfully ")
    return redirect('/login')

def login(request:HttpRequest):
    context={}
    if request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user= auth.authenticate(request=request, username=username,password=password)
            
            if user:
                auth.login(request=request,user=user)
                messages.success(request=request, message="You have login sucsessfully ")
                return redirect("/")
            messages.error(request=request, message="Fail to login user user not found")

        except Exception as e:
            messages.error(request=request, message="Fail to login user")
    return render(request,"login.html",context=context)

def register(request:HttpRequest):
    context={}
    if request.POST:
        password=request.POST.get('pwd')
        password2=request.POST.get('cpwd')
        
        if password2==password:
            try:
                user_name=request.POST.get('name')
                email=request.POST.get('Email')
                address=request.POST.get('Address')
                phone=request.POST.get("phone")
                photo=request.FILES.get("img")

                User.objects.create_user(username=user_name,email=email,password=password)
                user= auth.authenticate( request= request,username=user_name,password=password)
                auth.login(request=request,user=user)
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
                messages.success(request=request, message="Account created sucsessfully ")
                return redirect("/")
            except Exception as e :
                messages.error(request=request, message="Fail to create Account ")                
    return render(request,"register.html",context=context)