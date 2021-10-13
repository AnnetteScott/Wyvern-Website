from django.urls import path
from . import views


urlpatterns = [ 
    path('cookebook/', views.home, name="CookieBook"),
    path('cookebook/cooking/', views.cooking, name="Cooking"),
    path('cookebook/baking/', views.baking, name="Baking"),

    path('cookebook/cooking/<slug:recipename>/', views.cookingRecipe, name="CookingRecipe"),
    path('cookebook/baking/<slug:recipename>/', views.bakingRecipe, name="BakingRecipe"),
]