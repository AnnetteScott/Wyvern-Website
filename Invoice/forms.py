from django import forms
from django.utils.safestring import mark_safe

class ProjectForm(forms.Form):
    ProjectName = forms.CharField()
    MaxWeeks = forms.IntegerField()
    startDate = forms.DateField()