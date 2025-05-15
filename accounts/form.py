from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(AuthenticationForm):
    class Mata:
        model=User
        filds="__all__"
        
        
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=User
        fields=('username','email')
        
        