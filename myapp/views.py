from django.shortcuts import render
from myapp.forms import LoginForm
from . import models
from django.template import loader
from myapp.models import Student, Group, LabActivity, LabProcedure, StudentGroup, Profile, LabProcedureStatus
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

# Create your views here.
def home(request):
	if(request.user.is_authenticated):
		if request.method=='GET':
			func = request.GET.get('func')
			myid = request.GET.get('id')

			if(myid):
				labactivity = LabActivity.objects.get(labid=myid)
				labactivities = LabActivity.objects.all()

				if(func == '0'): # Select
					for labs in labactivities:
						labs.selected = False
						labs.save()
					labactivity.selected = True
					labactivity.hidden = False
					labactivity.save()
				elif(func == '1'): # Deselect
					labactivity.selected = False
					labactivity.save()
				elif(func == '2'): # Hide
					labactivity.hidden = True
					labactivity.selected = False
					labactivity.save()
				elif(func == '3'): # Unhide
					labactivity.hidden = False
					labactivity.save()

		uType = request.user.profile.userType
		context = {
			'labactivities': LabActivity.objects.all()
		}
		if(uType == False):
			# return render(request, "student.html", {})
			template = loader.get_template('student.html')
			myprofile = Profile.objects.get(user=request.user)
			myprofile.loggedin = True
			myprofile.save()
		else:
			# print(request.user.profile.facultyid.facultyname)
			# return render(request, "teacher.html", {})
			template = loader.get_template('teacher.html')

		return HttpResponse(template.render(context, request))

def logout(request):
	myprofile = Profile.objects.get(user=request.user)
	myprofile.loggedin = False
	myprofile.save()

	uType = request.user.profile.userType
	if(uType == True):
		labactivities = LabActivity.objects.get(selected=True)
		labactivities.selected = False
		labactivities.save()

	return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

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
	if request.method=='GET':
		id = request.GET.get('id')
	template = loader.get_template('student_labactivity.html')
	context = {
		'labprocedures': LabProcedure.objects.filter(labid=id),
		'labactivities': LabActivity.objects.filter(pk=id)
	}
	# return render(request, "student_labactivity.html", {})
	return HttpResponse(template.render(context, request))

def start(request):
	if request.method=='GET':
		id = request.GET.get('id')
	template = loader.get_template('student_labactivity_start.html')
	context = {
		'labprocedures': LabProcedure.objects.filter(labid=id),
		'labactivities': LabActivity.objects.filter(pk=id)
	}
	return HttpResponse(template.render(context, request))

# def teacher(request):
# 	return render(request, "teacher.html", {})

def labactivity(request):
	if request.method=='GET':
		id = request.GET.get('id')
	template = loader.get_template('teacher_labactivity.html')
	context = {
		'labprocedures': LabProcedure.objects.filter(labid=id),
		'labactivities': LabActivity.objects.filter(pk=id)
	}
	# return render(request, "student_labactivity.html", {})
	return HttpResponse(template.render(context, request))

def progresstracker(request):
	template = loader.get_template('teacher_progresstracker.html')
	context = {
		'studentgroups': StudentGroup.objects.filter(facultyid=request.user.profile.facultyid),
		'groups': Group.objects.all(),
		'students': Student.objects.all(),
		'profiles': Profile.objects.all(),
		'labactivities': LabActivity.objects.all(),
		'labprocedures': LabProcedure.objects.all(),
		# 'labprocedurestatuses': LabProcedureStatus.objects.all()
	}
	return HttpResponse(template.render(context, request))

def progresstracker_student(request):
	return render(request, "teacher_progresstracker_student.html", {})