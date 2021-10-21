from django.urls import path
from . import views


urlpatterns = [ 
    path('arcade/', views.home, name="Arcade"),
]