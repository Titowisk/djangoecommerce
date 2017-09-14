# coding=utf-8

from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import User
"""
Criou-se um modelo customizavel do Usuário. Então tem que criar
um modelo customizavel de fórmulario para poder criar o usuário em si.
Esse módulo também é utilizado para criar usuários normalmente (lá em core.views).
"""

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']
        # A classe herdada(UserCreationForm já possui o necessário para o password.

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']

