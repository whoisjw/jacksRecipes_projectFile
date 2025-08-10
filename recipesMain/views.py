from django.shortcuts import render

def listRecipesView(request):
    return render(request, "recipeViews/recipeList.html")

def expandRecipeView():
    return render(request, "recipeViews/recipeExpand.html")

def addRecipeView():
    return render(request, "recipeViews/recipeAdd.html")