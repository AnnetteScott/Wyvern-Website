from django.urls import path
from . import views


urlpatterns = [ 
    path('cookiebook/', views.home, name="CookieBook"),
]