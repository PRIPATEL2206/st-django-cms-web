from django.urls import path, re_path
from django.conf.urls.static import static
from cms_sales import settings
from django.views.static import serve

from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("login/",view=views.login,name="login"),
    path("logout/",view=views.logout,name="logout"),
    path("register/",view=views.register,name="register"),
    path("profile/",view=views.profile,name="profile"),
    path("addProduct/",view=views.addProductPage,name="addProduct"),
    path("addEmployee/",view=views.addEmployee,name="addEmployee"),
    path("cart/",view=views.cartPage,name="cart"),
    path("myOrders/",view=views.myOrders,name="myOrders"),
    path("ordersToAprove/",view=views.ordersToAprove,name="ordersToAprove"),
    path("allUsers/",view=views.allUsersPage,name="allUsers"),
    path("dashBord/",view=views.dashBord,name="dashBord"),
    path("user/<str:u_id>",view=views.userPage,name="user"),
    path("ordersToAprove/aproveOrder/<str:o_id>",view=views.aproveOrder,name="aproveOrder"),
    path("ordersToAprove/discardOrder/<str:o_id>",view=views.discardOrder,name="discardOrder"),
    path("ordersToAprove/shiping/<str:o_id>",view=views.shiping,name="shiping"),
    path("ordersToAprove/delivred/<str:o_id>",view=views.delivered,name="delivred"),
    path("ordersToAprove/<str:o_id>",view=views.orderAprovePage,name="orderAprovePage"),

    #add path 
    path("addToCart/<str:p_id>",view=views.addToCart,name="addToCart"),
    path("removeFromCart/<str:p_id>",view=views.removeFromCart,name="removeFromCart"),
    path("cart/buyCart/<str:c_id>",view=views.buyCart,name="buyCart"),
    
    # update
    path("cart/incrementProductQuntity/<str:p_id>",view=views.incrementProductQuntity,name="incrementProductQuntity"),
    path("cart/dicrementProductQuntity/<str:p_id>",view=views.dicrementProductQuntity,name="dicrementProductQuntity"),
    path("updateProfile/",view=views.updateProfile,name="updateProfile"),

]
if(settings.DEBUG):
    urlpatterns+=static(settings.STATIC_URL)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
else:
    urlpatterns+= re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),