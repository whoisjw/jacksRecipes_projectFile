from django.urls import path

from . import views

urlpatterns = [
    path("", views.listRecipeViews, name="listRecipeViews"),
    path("<int:recipeId>/", views.expandRecipeView, name="expandRecipeView"),   
]