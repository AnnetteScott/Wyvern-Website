from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import UserSetting

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        url = "/invoice/" + request.user.username + "/"
        return redirect(url)
    else:
        return render(request, 'Invoice/home.html')
    
def userHome(request, user_name):
    does_exist = False
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():      
            projectNameForm = (request.POST.get('ProjectName'))
            maxWeeksForm = (request.POST.get('MaxWeeks'))
            startDateForm = (request.POST.get('startDate'))
            if not UserSetting.objects.filter(user=user_name,projectName=projectNameForm).exists():
                new_entry = UserSetting(user=user_name, projectName=projectNameForm, maxWeeks=maxWeeksForm, lastWeek=2, startDate=startDateForm)
                new_entry.save()
                form = ProjectForm()
            else:
                does_exist = True
            
    else:
        form = ProjectForm()
    context = {'form': form, 'exists': does_exist}
    return render(request, 'Invoice/userHome.html', context)