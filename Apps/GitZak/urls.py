from django.urls import path
from . import views


urlpatterns = [ 
    path('Zak/', views.home, name="GitZak"),
]