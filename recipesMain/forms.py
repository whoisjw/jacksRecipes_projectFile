from django import forms 
from django.forms import ModelForm, Textarea
from recipesMain.models import recipe, ingredientRelations

class addRecipe(ModelForm):
    class Meta: 
        model = recipe
        widgets = {
            "title": Textarea(attrs={"placeholder":"Enter a fitting title...", "rows":1, "cols": 32}),
            "ingredients": Textarea(attrs={"placeholder":"Enter your recipe's ingredients here...", "rows":10, "cols":128}),
            "body": Textarea(attrs={"placeholder":"Enter your instructions here...", "rows":15, "cols": 128})
        }
        fields = [
            "title",
            "image",
            "ingredients",
            "body",
            "tag"
        ]

class addIngredient(ModelForm):
    class Meta:
        model = ingredientRelations

        widgets = {
            "notes": Textarea(attrs={"placeholder":"Any notes?", "rows":2, "cols":64})
        }

        fields = [
            "ingredient",
            "quantity",
            "unit",
            "notes"
        ]
