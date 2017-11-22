#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from myapp.models import Student, StudentGroup

class LoginForm(AuthenticationForm):
   username = forms.CharField(label="Username", max_length= 30,
								widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
   password = forms.CharField(label="Password", max_length= 30,
								widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class StudentForm(forms.ModelForm):
	studentname = forms.CharField(label="Student Name", max_length= 80,
								widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'studentname'}))
	class Meta:
		model = Student
		fields = ('studentname',)

class GroupForm(forms.ModelForm):
	username = forms.CharField(label="Username", max_length= 30,
								widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	groupname = forms.CharField(label="Group Name", max_length= 80,
								widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'groupname'}))
	password = forms.CharField(label="Group Name", max_length= 30,
								widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
	repassword = forms.CharField(label="Group Name", max_length= 30,
								widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'repassword'}))

	class Meta:
		model = StudentGroup
		fields = ('groupname',)