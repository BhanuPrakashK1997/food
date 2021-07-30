from django.db import models
from django.utils import timezone


# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=25)
    ingredients = models.TextField(max_length=200)
    process = models.TextField()
    image = models.FileField(upload_to="pictures/")

    def __str__(self):
        return self.name