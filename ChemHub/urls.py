from django.urls import path
from . import views


urlpatterns = [ 
    path('ChemHub/', views.home, name="ChemHub"),
]