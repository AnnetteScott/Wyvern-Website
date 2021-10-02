from django.urls import path
from . import views


urlpatterns = [ 
    path('NotDie/', views.home, name="HowToNotDie101"),
]