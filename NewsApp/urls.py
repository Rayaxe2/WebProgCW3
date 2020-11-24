from django.urls import path
from NewsApp import views

urlpatterns = [
    path('', views.Index, name='MainPage'),
    path('signup/', views.SignUp, name='SignUp'),
    path('signup/register/', views.SignUpHandler, name='SignUpHandler'),
    path('login/', views.LogIn, name='LogIn'),
    path('login/Signin/', views.LoginHandler, name='LoginHandler'),
    path('logout/', views.LogOut, name='LogOut'),
]