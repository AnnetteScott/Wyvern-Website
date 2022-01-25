from genericpath import exists
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
    user_has_projects = False
    projectList = []
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():      
            projectNameForm = (request.POST.get('ProjectName'))
            maxWeeksForm = (request.POST.get('MaxWeeks'))
            startDateForm = (request.POST.get('startDate'))
            new_url = projectNameForm.replace(" ", "-")
            if not UserSetting.objects.filter(user=user_name,projectName=projectNameForm).exists():
                new_entry = UserSetting(user=user_name, projectName=projectNameForm, maxWeeks=maxWeeksForm, lastWeek=2, startDate=startDateForm, url=new_url)
                new_entry.save()
                form = ProjectForm()
            else:
                does_exist = True
            
    else:
        form = ProjectForm()

    if UserSetting.objects.filter(user=user_name).exists():
        user_has_projects = True
        projectList = UserSetting.objects.filter(user=user_name)

    context = {'form': form, 'exists': does_exist, 'projectList': projectList, 'user_has_projects': user_has_projects}
    return render(request, 'Invoice/userHome.html', context)

def projectHome(request, user_name, project_name):
    selectedProject = UserSetting.objects.filter(user=user_name,url=project_name).values()[0]

    
    context = {'selectedProject': selectedProject}
    return render(request, 'Invoice/project.html', context) 