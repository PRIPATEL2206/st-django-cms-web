from django.urls import path
from django.conf.urls.static import static
from cms_sales import settings

from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("login/",view=views.login,name="login"),
    path("register/",view=views.register,name="register"),

]
if(settings.DEBUG):
    urlpatterns+=static(settings.STATIC_URL)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
