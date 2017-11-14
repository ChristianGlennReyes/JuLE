from django.shortcuts import render
from myapp.forms import LoginForm
from . import models
from django.template import loader
from myapp.models import Student
from myapp.models import Group
from myapp.models import LabActivity
from django.http import HttpResponse

# Create your views here.
def home(request):
	if(request.user.is_authenticated):
		uType = request.user.profile.userType
		context = {
			'labactivities': LabActivity.objects.all()
		}
		if(uType == False):
			# return render(request, "student.html", {})
			template = loader.get_template('student.html')
			return HttpResponse(template.render(context, request))
		else:
			# print(request.user.profile.facultyid.facultyname)
			# return render(request, "teacher.html", {})
			template = loader.get_template('teacher.html')
			return HttpResponse(template.render(context, request))

# def student(request):
# 	return render(request, "student.html", {})

def student_members(request):
	template = loader.get_template('student_members.html')
	context = {
		# 'students': Student.objects.all()
		'students': Student.objects.filter(group__groupid=request.user.profile.groupid)
	}
	return HttpResponse(template.render(context, request))

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