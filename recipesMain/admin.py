from django.contrib import admin
from .models import recipe, category, ingredientRelations, instructions

admin.site.register(recipe)
admin.site.register(category)
admin.site.register(ingredientRelations)
admin.site.register(instructions)