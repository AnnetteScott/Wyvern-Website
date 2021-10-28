from django.urls import path
from . import views


urlpatterns = [ 
    path('arcade/', views.home, name="Arcade"),
    path('arcade/<slug:gameurl>/', views.gamePage, name="ArcadeGame"),
    path('arcade/exploding-kacti/add_score/', views.add_score),
]