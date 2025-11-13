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
    prepTime = models.IntegerField(default=15)
    cookTime = models.IntegerField(default=20)
    ingredients = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to="food_images/", default="food_images/icon.png")
    tag = models.ManyToManyField(category, db_column = "categoryTitle")

    class Meta:
        db_table = "recipe"

    def __str__(self):
        return self.title

class ingredientRelations(models.Model):
    relationId = models.BigAutoField(primary_key = True)
    recpieId = models.ForeignKey(recipe, on_delete=models.CASCADE)
    ingredient = models.TextField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    notes = models.CharField(max_length=100)

    class Meta:
        db_table = "ingredientRelations"

    def __str__(self):
        return self.ingredient

class instructions(models.Model): 
    instructionId = models.BigAutoField(primary_key = True)
    recipeId = models.ForeignKey(recipe, on_delete=models.CASCADE)
    stepNumber = models.IntegerField()
    stepBody = models.TextField(max_length=300)

    class Meta:
        db_table = "instructions"

    def __str__(self):
        return self.stepNumber