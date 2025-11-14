from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from recipesMain.models import category, recipe, ingredientRelations, instructions
from recipesMain.forms import addRecipe, addIngredient
from django.db.models import Q
from django.core.paginator import Paginator as P
from django.conf import settings

def listRecipesView(request):
    #search for database entries
    categories = category.objects.all()
    q = request.GET.get("q", default="")
    tagDDM = request.GET.get("tagDDM", default="")

    recipesDisp = recipe.objects.filter((Q(title__icontains=q) | 
                                        Q(body__icontains=q)) & 
                                        Q(tag__categoryTitle__icontains=tagDDM))

    #handle pagination
    paginator = P(recipesDisp, 4)
    pageObj = paginator.get_page(request.GET.get('page'))

    return render(request, "recipeViews/recipeList.html", {"category": categories, "pageObj": pageObj,})

def expandRecipeView(request, recipeId):
    id = recipeId

    try:
        recipesDisp = recipe.objects.get(pk=id)
        recipeRequest = HttpResponse("This is recipe %s" % id)
    except:
        raise Http404("Recipe does not exist. Maybe you should write it!")

    try:
        recipesIngredients = ingredientRelations.objects.get(recpieId_id=id)
    except:
        raise Http404("Error: could not load recipe steps")
    return render(request, "recipeViews/recipeExpand.html", {"recipesDisp": recipesDisp, "recipesIngredients":recipesIngredients})

def addRecipeView(request):
    recipesForm = addRecipe

    if request.method == "POST":
        recipesForm = addRecipe(request.POST, request.FILES)
        ingredientsForm = addIngredient(request.POST)
        if recipesForm.is_valid() and ingredientsForm.is_valid():
            newRecipe = recipesForm.save(commit=False)
            newRecipe.save()
            newIngList = ingredientsForm.save(commit=False)
            newIngList.save()
            recipesForm.save()
            ingredientsForm.save()
            return redirect("/recipes/" + str(newRecipe.recipeId))

    return render(request, "recipeViews/recipeAdd.html", {"recipesForm": recipesForm})