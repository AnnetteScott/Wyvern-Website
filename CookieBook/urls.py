from django.urls import path
from . import views


urlpatterns = [ 
    path('cookebook/', views.home, name="CookieBook"),
    path('cookebook/<slug:recipe_type>/', views.recipeList, name="Type_Recipe"),

    path('cookebook/<slug:recipe_type>/<slug:recipename>/', views.recipePage, name="RecipePage"),
]