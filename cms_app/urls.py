from django.urls import path
from django.conf.urls.static import static
from cms_sales import settings

from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("login/",view=views.login,name="login"),
    path("register/",view=views.register,name="register"),
    path("profile/",view=views.profile,name="profile"),
    path("addProduct/",view=views.addProductPage,name="addProduct"),
    path("cart/",view=views.cartPage,name="cart"),

    #add path 
    path("addToCart/<str:p_id>",view=views.addToCart,name="updateProfile"),
    path("removeFromCart/<str:p_id>",view=views.removeFromCart,name="removeFromCart"),
    
    # update
    path("updateProfile/",view=views.updateProfile,name="updateProfile"),

]
if(settings.DEBUG):
    urlpatterns+=static(settings.STATIC_URL)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
