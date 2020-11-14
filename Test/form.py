from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserAnswerForm(ModelForm):
    class Meta:
        model = UsersTest
        fields = ['usersanswer', 'user', 'test_kits']