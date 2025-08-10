from django.contrib import admin
from .models import recipe, category

admin.site.register(recipe)
admin.site.register(category)