from django.urls import path
from . import views

urlpatterns = [ 
    path('signup/', views.SignUp_view, name="SignUp"),
    path('login/', views.LogIn_view, name="Login"),
    path('logout/', views.Logout_view, name="Logout"),
]