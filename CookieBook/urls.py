from django.urls import path
from . import views


urlpatterns = [ 
    path('cookiebook/', views.home, name="CookieBook"),
    path('cookiebook/cooking/', views.cooking, name="Cooking"),
    path('cookiebook/baking/', views.baking, name="Baking"),
]