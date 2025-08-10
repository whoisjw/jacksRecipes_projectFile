from django.shortcuts import render
from django.http import Http404, HttpResponse
from recipesMain.models import category, recipe

def listRecipesView(request):
    categories = category.objects.all()

    recipesDisp = recipe.objects.all()

    return render(request, "recipeViews/recipeList.html", {"recipesDisp": recipesDisp})

def expandRecipeView(request, recipeId):
    try:
        recipesDisp = recipe.objects.get(pk=recipeId)
        recipeRequest = HttpResponse("This is recipe %s" % recipeId)
    except:
        raise Http404("Recipe does not exist. Maybe you should write it!")
    return render(request, "recipeViews/recipeExpand.html", {"recipesDisp": recipesDisp})

def addRecipeView():
    return render(request, "recipeViews/recipeAdd.html")