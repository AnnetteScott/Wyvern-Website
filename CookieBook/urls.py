from django.urls import path
from . import views


urlpatterns = [ 
    path('cookiebook/', views.home, name="CookieBook"),
    path('cookiebook/cooking/', views.cooking, name="Cooking"),
    path('cookiebook/baking/', views.baking, name="Baking"),

    path('cookiebook/cooking/<slug:recipename>/', views.cookingRecipe, name="CookingRecipe"),
    path('cookiebook/baking/<slug:recipename>/', views.cookingRecipe, name="BakingRecipe"),
]