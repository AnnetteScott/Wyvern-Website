from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(label='Enter some things here', widget=forms.Textarea)