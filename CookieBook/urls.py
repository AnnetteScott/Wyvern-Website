from django.urls import path
from . import views


urlpatterns = [ 
    path('cookebook/', views.home, name="CookieBook"),
    path('cookebook/<slug:the_type_of_recipe>/', views.recipeList, name="RecipePage"),
    path('cookebook/<slug:the_type_of_recipe>/<slug:recipename>/', views.recipePage, name="RecipePage"),
]