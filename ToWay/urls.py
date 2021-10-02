from django.urls import path
from . import views


urlpatterns = [ 
    path('ToWay/', views.home, name="ToWay"),
]