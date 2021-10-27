from django.db import models

# Create your models here.
class GamesList(models.Model):
    title = models.CharField(max_length=100)
    img = models.FileField(upload_to='static/Images/Arcade', null=True, blank=True)
    online = models.BooleanField()
    url = models.CharField(max_length=20, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class ExplodingKactiScore(models.Model):
    score = models.IntegerField()    
    name = models.CharField(max_length=8, blank=True)
    
    def __str__(self):
        return str(self.name)