from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(label='new label', widget=forms.Textarea)