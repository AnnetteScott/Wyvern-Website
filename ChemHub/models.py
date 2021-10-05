from django.db import models

# Create your models here.

class Element(models.Model):
    name = models.CharField(max_length=50)
    atomic_number = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    melting = models.CharField(max_length=50)
    boiling = models.CharField(max_length=50)
    density = models.CharField(max_length=50)
    electron = models.CharField(max_length=50)