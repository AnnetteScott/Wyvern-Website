from django.urls import path
from . import views


urlpatterns = [ 
    path('hazards101/', views.home, name="HowToNotDie101"),
]