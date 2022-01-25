from django.urls import path
from . import views

urlpatterns = [ 
    path('invoice/', views.home, name="Invoice"),
    path('signup/', views.SignUp, name="SignUp"),
    path('signin/', views.SignIn, name="SignIn"),
]