from django.urls import path
from . import views

urlpatterns = [ 
    path('whattodo/', views.home, name="WhatToDo"),
]