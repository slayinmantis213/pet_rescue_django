from django.urls import path     
from . import views

app_name = "users"

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name="register"),
    path('new_user/', views.newuser, name ="help"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),	   
    path('dashboard/', views.userdash, name="dashboard")
]