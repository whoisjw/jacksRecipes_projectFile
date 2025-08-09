from django.db import models

class recipe(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    image = models.ForeignKey(recipeImage, on_delere = models.CASCADE)
    tag = models.ManyToManyField(caregoryTitle)

    def __str__(self):
        return self.title

class category(models.Model):
    categoryTitle = models.CharField(max_length = 30)

    def __str__(self):
        return self.categoryTitle
        
class image(models.Model):
    imageTitle = models.CharField(max_length = 30)
    recipeImage = models.ImageField()

    def __str__(self):
        return self.imageTitle
