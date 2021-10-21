from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400, null=True, blank=True)
    cooking_time = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=1000)
    directions = models.CharField(max_length=2000)
    tag = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    first_letter = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
