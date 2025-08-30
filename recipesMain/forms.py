from django import forms 
from django.forms import ModelForm, Textarea
from recipesMain.models import recipe

class addRecipe(ModelForm):
    class Meta: 
        model = recipe
        widgets = {
            "ingredients": Textarea(attrs={"rows":6, "cols":30}),
            "body": Textarea(attrs={"rows":10, "cols": 30})
        }
        fields = ["title", 
                "ingredients",
                "body",]
