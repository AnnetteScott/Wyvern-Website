from django.urls import path
from . import views


urlpatterns = [ 
    path('netty/', views.home, name="NettyHub"),
]