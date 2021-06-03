from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



user = get_user_model()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='ef'
        self.fields['username'].widget.attrs['type']='text'
        self.fields['username'].widget.attrs['id']='shimei'
        self.fields['password'].widget.attrs['class']='ef'
        self.fields['password'].widget.attrs['type']='password'
        self.fields['password'].widget.attrs['id']='pas'

class Signform(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.fields['username'].widget.attrs['class']='ef'
        self.fields['username'].widget.attrs['id']='shimei'
        self.fields['password1'].widget.attrs['class']='ef'
        self.fields['password1'].widget.attrs['id']='pas'
        self.fields['password2'].widget.attrs['class']='ef'
        self.fields['password2'].widget.attrs['id']='pas'
    
    class Meta:
        model = User 
        fields = ("username","password1","password2",)