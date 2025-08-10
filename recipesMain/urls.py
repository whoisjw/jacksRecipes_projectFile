from django.urls import path

from . import views

urlpatterns = [
    path("", views.listRecipesView, name="listRecipesView"),
    path("<int:recipeId>/", views.expandRecipeView, name="expandRecipeView"),   
]