from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from recipesMain.models import category, recipe
from recipesMain.forms import addRecipe

def listRecipesView(request):
    categories = category.objects.all()
    q = request.GET.get("q")
    tag = request.GET.get("tag")

    recipesDisp = recipe.objects.all()

    return render(request, "recipeViews/recipeList.html", {"recipesDisp": recipesDisp})

def expandRecipeView(request, recipeId):
    try:
        recipesDisp = recipe.objects.get(pk=recipeId)
        recipeRequest = HttpResponse("This is recipe %s" % recipeId)
    except:
        raise Http404("Recipe does not exist. Maybe you should write it!")
    return render(request, "recipeViews/recipeExpand.html", {"category": categories}, {"recipesDisp": recipesDisp})

def addRecipeView(request):
    recipesForm = addRecipe

    if request.method == "POST":
        recipesForm = addRecipe(request.POST)
        if recipesForm.is_valid():
            newRecipe = recipesForm.save(commit=False)
            newRecipe.save()
            recipesForm.save()
            return redirect("/recipes/" + str(newRecipe.recipeId))

    return render(request, "recipeViews/recipeAdd.html", {"recipesForm": recipesForm})