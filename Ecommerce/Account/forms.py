from django import forms
from django.contrib.auth.models import User

class sign_in_form(forms.Form):
    username = forms.CharField(label="username", max_length=100, required=True)
    password = forms.CharField(label="password",widget=forms.PasswordInput(), required=True)
    
class sign_up_form(forms.Form):
    username = forms.CharField(label="username", max_length=100, required=True)
    password = forms.CharField(label="password",widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(label="email", required=True)
