from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserInputForm
import random

def home(request):
    chosen = None
    button_value = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():      
            user_input = (request.POST.get('user_input')).split('\n')
            random_num = random.randrange(0, len(user_input))
            chosen = user_input[random_num]
            button_value = "Re-Submit"
    else:
        form = UserInputForm()
        button_value = "Submit"

    context = {'form': form, 'chosen': chosen, 'Button_Value': button_value}
    return render(request, 'WhatToDo/home.html', context)