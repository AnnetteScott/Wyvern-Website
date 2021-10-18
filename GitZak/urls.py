from django.urls import path
from . import views


urlpatterns = [ 
    path('giga/', views.home, name="GitZak"),
]