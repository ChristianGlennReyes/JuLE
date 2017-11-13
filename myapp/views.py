from django.shortcuts import render

from myapp.forms import LoginForm
from . import models
# Create your views here.
def home(request):
	if(request.user.is_authenticated):
		uType = request.user.profile.userType
		if(uType == False):
			return render(request, "student.html", {})
		else:
			print(request.user.profile.facultyid.facultyname)
			return render(request, "teacher.html", {})

# def student(request):
# 	return render(request, "student.html", {})

def student_members(request):
	return render(request, "student_members.html", {})

def lab_activity(request):
	return render(request, "student_labactivity.html", {})

def start(request):
	return render(request, "student_labactivity_start.html", {})

# def teacher(request):
# 	return render(request, "teacher.html", {})

def labactivity(request):
	return render(request, "teacher_labactivity.html", {})

def progresstracker(request):
	return render(request, "teacher_progresstracker.html", {})

def progresstracker_student(request):
	return render(request, "teacher_progresstracker_student.html", {})
