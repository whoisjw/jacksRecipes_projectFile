from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from recipesMain.models import category, recipe
from recipesMain.forms import addRecipe
from django.db.models import Q
from django.core.paginator import Paginator as P

def listRecipesView(request):
    categories = category.objects.all()
    q = request.GET.get("q", default="")
    tagDDM = request.GET.get("tagDDM", default="")

    recipesDisp = recipe.objects.filter((Q(title__icontains=q) | 
                                        Q(body__icontains=q)) & 
                                        Q(tag__categoryTitle__icontains=tagDDM))

    paginator = P(recipesDisp, 2)
    pageObj = paginator.get_page(request.GET.get('page'))

    return render(request, "recipeViews/recipeList.html", {"category": categories, "pageObj": pageObj})

def expandRecipeView(request, recipeId):
    try:
        recipesDisp = recipe.objects.get(pk=recipeId)
        recipeRequest = HttpResponse("This is recipe %s" % recipeId)
    except:
        raise Http404("Recipe does not exist. Maybe you should write it!")
    return render(request, "recipeViews/recipeExpand.html", {"recipesDisp": recipesDisp})

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