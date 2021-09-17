from typing import Sequence
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.enums import TextChoices
from . import models

class create_course_form(forms.Form):
    title = forms.CharField(label='موضوع:',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "موضوع",
                "class": "form-control my-3",
                'autocomplete': 'false',
            }
        ))
    description = forms.CharField(label='توضیحات:',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "توضیحات",
                "class": "form-control my-3",
                'autocomplete': 'false',
            }
        ))

class create_lesson_form(forms.Form):
    key = forms.CharField(label='سوال:',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "سوال",
                "class": "form-control my-3",
                'autocomplete': 'false',
            }
        ))
    value = forms.CharField(label='جواب:',
        widget=forms.Textarea(
            attrs={
                "placeholder" : "جواب",
                "class": "form-control my-3",
                'autocomplete': 'false',
            }
        ))
        

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "نام کاربری",
                "class": "form-control my-3"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "رمز عبور",
                "class": "form-control my-3"
            }
        ))