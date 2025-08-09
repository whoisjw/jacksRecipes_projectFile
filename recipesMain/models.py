from django.db import models

class recipe(models.Model):
    recipeId = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    body = models.TextField()
    image = models.ForeignKey(recipeImage, on_delere = models.CASCADE)
    tag = models.ManyToManyField(caregoryTitle)

    class Meta:
        db_table = "recipe"

    def __str__(self):
        return self.title

class category(models.Model):
    categoryId = models.BigAutoField(primary_key = True)
    categoryTitle = models.CharField(max_length = 30)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryTitle
        
class image(models.Model):
    imageId = models.BigAutoField(primary_key = True)
    imageTitle = models.CharField(max_length = 30)
    recipeImage = models.ImageField()

    class Meta:
        db_table = "image"

    def __str__(self):
        return self.imageTitle
