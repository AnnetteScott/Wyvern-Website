from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(label='Enter Each Item On a New Line:', widget=forms.Textarea)