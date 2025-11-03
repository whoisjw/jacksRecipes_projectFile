from django import forms 
from django.forms import ModelForm, Textarea
from recipesMain.models import recipe

class addRecipe(ModelForm):
    class Meta: 
        model = recipe
        widgets = {
            "ingredients": Textarea(attrs={"rows":10, "cols":64}),
            "body": Textarea(attrs={"rows":20, "cols": 64})
        }
        fields = ["title",
                "image",
                "ingredients",
                "body",
                "tag"]
