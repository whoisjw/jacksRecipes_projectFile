from django.urls import path
from .models import recipe

from . import views

urlpatterns = [
    path("", views.listRecipesView, name="listRecipesView"),
    path("<int:recipeId>/", views.expandRecipeView, name="expandRecipeView"),  
    path("add/", views.addRecipeView, name="addRecipeView") 
]