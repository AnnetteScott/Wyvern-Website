from django.urls import path
from . import views

urlpatterns = [ 
    path('invoice/', views.home, name="Invoice"),
    path('invoice/<slug:user_name>/', views.userHome, name="UserHome"),
    path('invoice/<slug:user_name>/<slug:project_name>/', views.projectHome, name="UserProject"),
]