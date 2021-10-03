from django.urls import path
from . import views


urlpatterns = [ 
    path('toway/', views.home, name="ToWay"),
]