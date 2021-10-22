from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserInputForm
import random

form = None

def result(request):
    chosen = None
    user_input = (request.POST.get('user_input')).split('\n')
    random_num = random.randrange(0, len(user_input))
    chosen = user_input[random_num]
    context = {'chosen': chosen}
    return render(request, 'WhatToDo/result.html', context )


def home(request):
    form = UserInputForm()
    context = {'form': form}
    return render(request, 'WhatToDo/home.html', context)