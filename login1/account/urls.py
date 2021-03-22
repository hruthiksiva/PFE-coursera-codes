from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('home',views.home,name="home"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('registerdetails',views.registerdetails,name="registerdetails"),
]