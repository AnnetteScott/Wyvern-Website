from django.urls import path
from . import views


urlpatterns = [ 
    path('invoice/', views.home, name="Invoice"),
    path('invoice/signup/', views.SignUp, name="SignUp"),
    path('invoice/signin/', views.SignIn, name="SignIn"),
]