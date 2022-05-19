from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(max_length=32)
    password = forms.CharField()