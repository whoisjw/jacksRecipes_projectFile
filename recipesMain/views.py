from django.shortcuts import render

def listRecipesView():
    return render(request, "recipeViews/recipeList.html")

def expandRecipeView():
    return render (request, "recipeViews/recipeExpand.html")