import email
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cms_app.models import CMSUser
from cms_app.models import ROLES

@login_required(login_url="/login",redirect_field_name="home")
def index(request):
    return render(request=request,template_name="index.html")

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