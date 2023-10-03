# from django import forms
from typing import Any
from django.forms import CharField, EmailField, PasswordInput, ValidationError
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserRegistrationForm(UserCreationForm):
    username = CharField(label='username', min_length=5, max_length=20)
    email = EmailField(label='email')
    password1 = CharField(label='password',widget=PasswordInput)
    password2 = CharField(label='confirm password', widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email',]
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        
        if User.objects.filter(username=username).exists():
            raise ValidationError('User already exists.')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with this email already exists.')
        return email

    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['passsword2']
        
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError('Passwords do not match.')
    #     return password2
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match.')
        
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        print(user)