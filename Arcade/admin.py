from django.contrib import admin

# Register your models here.
from .models import ExplodingKactiScore, GamesList
admin.site.register(GamesList)
admin.site.register(ExplodingKactiScore)