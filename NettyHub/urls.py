from django.urls import path
from . import views


urlpatterns = [ 
    path('Netty/', views.home, name="NettyHub"),
]