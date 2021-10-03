from django.urls import path
from . import views


urlpatterns = [ 
    path('zak/', views.home, name="GitZak"),
]