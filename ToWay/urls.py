from django.urls import path
from . import views


urlpatterns = [ 
    path('whichway/', views.home, name="ToWay"),
]