from django import forms

class NameForm(forms.Form):
    user_input = forms.Textarea(label='user input', max_length=1000)