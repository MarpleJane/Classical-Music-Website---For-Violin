from django import forms
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username=forms.CharField(required=True,label='username',
                             error_message={'required':'please input the username'},
                             widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(required=True,label='password',
                             error_message={'required':'please input the password'},
                             widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    
