from django.shortcuts import render
from .models import GamesList

# Create your views here.
def home(request):
    games_list_dict = list(GamesList.objects.values())
    context = {'games_list': games_list_dict}
    return render(request, 'Arcade/home.html', context)

