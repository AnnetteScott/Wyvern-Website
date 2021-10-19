from django.db import models

# Create your models here.
class Element(models.Model):
    name = models.CharField(max_length=50)
    atomic_number = models.CharField(max_length=50)
    mass = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    electron = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    melting = models.CharField(max_length=50, null=True, blank=True)
    boiling = models.CharField(max_length=50, null=True, blank=True)
    sublimation = models.CharField(max_length=50, null=True, blank=True)
    density_at_stp = models.CharField(max_length=50, null=True, blank=True)
    density_at_rt = models.CharField(max_length=50, null=True, blank=True)
    density_at_mp = models.CharField(max_length=50, null=True, blank=True)
    triple_point = models.CharField(max_length=50, null=True, blank=True)
    critical_point = models.CharField(max_length=50, null=True, blank=True)
    heat_capacity = models.CharField(max_length=50, null=True, blank=True)
    ox_state = models.CharField(max_length=50, null=True, blank=True)
    en = models.CharField(max_length=50, null=True, blank=True)



    def __str__(self):
        return str(self.name)