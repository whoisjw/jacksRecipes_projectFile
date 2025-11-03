from django.db import models

class category(models.Model):
    categoryId = models.BigAutoField(primary_key = True)
    categoryTitle = models.CharField(max_length = 30)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryTitle  

class recipe(models.Model):
    recipeId = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    ingredients = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to="food_images/", default="food_images/icon.png")
    tag = models.ManyToManyField(category, db_column = "categoryTitle")

    class Meta:
        db_table = "recipe"

    def __str__(self):
        return self.title

