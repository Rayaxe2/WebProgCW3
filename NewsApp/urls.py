from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='MainPage'),
    path('signup/', views.SignUp, name='SignUp'),
    path('resigster/', views.SignUpHandler, name='SignUpHandler')
]