from django.urls import path
from . import views


urlpatterns = [ 
    path('toway/', views.ToWay, name="ToWay"),
]