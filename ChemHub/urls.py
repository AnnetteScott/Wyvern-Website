from django.urls import path
from . import views


urlpatterns = [ 
    path('chemhub/', views.home, name="ChemHub"),
]