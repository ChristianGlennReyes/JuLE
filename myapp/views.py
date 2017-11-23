from django.shortcuts import render, redirect
from myapp.forms import LoginForm, StudentForm, GroupForm
from . import models, forms
from django.template import loader
from myapp.models import Student, Group, LabActivity, LabProcedure, StudentGroup, Profile, LabProcedureStatus
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User

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

				return redirect('home')

		uType = request.user.profile.userType
		context = {
			'labactivities': LabActivity.objects.all()
		}
		if(uType == False):
			# return render(request, "student.html", {})
			template = loader.get_template('student.html')
		else:
			# print(request.user.profile.facultyid.facultyname)
			# return render(request, "teacher.html", {})
			template = loader.get_template('teacher.html')

		myprofile = Profile.objects.get(user=request.user)
		myprofile.loggedin = True
		myprofile.save()

		# stud = Student(studentname='Practice Lang')
		# stud.save()

		return HttpResponse(template.render(context, request))

def logout(request):
	myprofile = Profile.objects.get(user=request.user)
	myprofile.loggedin = False
	myprofile.save()

	uType = request.user.profile.userType
	if(uType == True):
		try:
			lab = LabActivity.objects.get(selected=True)
		except LabActivity.DoesNotExist:
			lab = None
		if(lab != None):
			lab.selected = False
			lab.save()

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
		labid = request.GET.get('id')

	labprocedures = LabProcedure.objects.filter(labid=labid)
	labactivities = LabActivity.objects.filter(pk=labid)

	initiallabproceddure = 0
	ctr = 0
	for labprocedure in labprocedures:
		if(ctr == 0):
			initiallabproceddure = labprocedure.procedureid
		ctr = ctr + 1

	return render(request, "student_labactivity_start.html", locals())

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

def group(request):
	studentgroups = StudentGroup.objects.filter(facultyid=request.user.profile.facultyid)
	groups = Group.objects.all()
	students = Student.objects.all()
	profiles = Profile.objects.all()
	labactivities = LabActivity.objects.all()
	labprocedures = LabProcedure.objects.all()
	labprocedurestatus = LabProcedureStatus.objects.all()
	
	# progress = {'group1':10}
	return render(request, "teacher_group.html", locals())

def group_labactivity(request):
	return render(request, "teacher_group_student.html", locals())

def addgroup(request):
	students = Student.objects.filter(facultyid=request.user.profile.facultyid)
	groups = Group.objects.all()

	namelists = []

	for student in students:
		ctr = False
		for group in groups:
			if(student == group.studentid):
				ctr = True
		if(ctr == False):
			namelists.append(student.studentname)

	if(request.method=="POST"):
		form = forms.GroupForm(request.POST)
		if form.is_valid():
			curruser = request.user.profile.facultyid
			username = form.cleaned_data['username']
			groupname = form.cleaned_data['groupname']
			password = form.cleaned_data['password']
			repassword = form.cleaned_data['repassword']
			selected = request.POST.getlist('selectedstudents')

			if(StudentGroup.objects.filter(groupname=groupname)):
				print('Group already exist')
			else:
				if(password == repassword):
					studentgroup = StudentGroup(facultyid=request.user.profile.facultyid, groupname=groupname)
					studentgroup.save()
					user = User.objects.create_user(username=username, password=password)
					studentgroup = StudentGroup.objects.get(groupname=groupname)
					profile = Profile(user=user, userType=0, facultyid=request.user.profile.facultyid, groupid=studentgroup, loggedin=0)
					profile.save()

					for selects in selected:
						student = Student.objects.get(studentname=selects)
						group = Group(groupid=studentgroup, studentid=student)
						group.save()

					if request.POST.get("saveadd"):
						return redirect('addgroup')
					elif request.POST.get("save"):
						return redirect('group')	

				else:
					print('Wrong Password')

	else:
		form = forms.GroupForm()

	return render(request, "teacher_group_add.html", locals())	

def editgroup(request):
	if request.method=='GET':
		myid = request.GET.get('id')
		studentgroups = StudentGroup.objects.filter(groupid=myid)

		for mystudentgroup in studentgroups:
			profiles = Profile.objects.filter(groupid=mystudentgroup)
			groups = Group.objects.filter(groupid=mystudentgroup)

		for myprofile in profiles:
			users = User.objects.filter(username=myprofile)

		students = Student.objects.filter(facultyid=request.user.profile.facultyid)
		mygroups = Group.objects.all()
		
		namelists = []

		for student in students:
			ctr = False
			for group in mygroups:
				if(student == group.studentid):
					ctr = True
			if(ctr == False):
				namelists.append(student.studentname)

	if request.POST.get("delete"):
		groups = Group.objects.filter(groupid=request.GET.get('id'))
		for group in groups:
			group.delete()
		profiles = Profile.objects.filter(groupid=request.GET.get('id'))
		for profile in profiles:
			users = User.objects.filter(username=profile.user)
			for user in users:
				user.delete()
			profile.delete()
		studentgroups = StudentGroup.objects.filter(groupid=request.GET.get('id'))
		for studentgroup in studentgroups:
			studentgroup.delete()
		return redirect('group')
	elif request.POST.get("save"):
		studentgroup = StudentGroup.objects.get(groupid=request.GET.get('id'))
		if studentgroup.groupname == request.POST['groupname']:
			print('Same groupname')
		else:
			studentgroups = StudentGroup.objects.filter(groupname=request.POST['groupname'], facultyid=request.user.profile.groupid)
			if studentgroups:
				print('Student group name already exists')
			else:
				savegroupname = StudentGroup.objects.get(groupid=request.GET.get('id'))
				savegroupname.groupname = request.POST['groupname']
				savegroupname.save()

		profile = Profile.objects.get(groupid=studentgroup)
		user = User.objects.get(username=profile.user)
		if user.username == request.POST['username']:
			print('Same username')
		else:
			users = User.objects.filter(username=request.POST['username'])
			if users:
				print('Username already exists')
			else:
				user.username = request.POST['username']
				user.save()

		ingroups = request.POST.getlist('ingroup')

		for ingroup in ingroups:
			student = Student.objects.get(studentname=ingroup)
			group = Group.objects.filter(studentid=student)
			if group:
				print('Has group')
			else:
				newGroup = Group(groupid=studentgroup, studentid=student)
				newGroup.save()

		nogroups = request.POST.getlist('nogroup')

		for nogroup in nogroups:
			student = Student.objects.get(studentname=nogroup)
			group = Group.objects.filter(studentid=student)
			if group:
				for mygroup in group:
					mygroup.delete()
			else:
				print('No group')

		return redirect('group')

	return render(request, "teacher_group_edit.html", locals())		

def student(request):
	template = loader.get_template('teacher_student.html')
	context = {
		'students': Student.objects.filter(facultyid=request.user.profile.facultyid)
	}
	return HttpResponse(template.render(context, request))

def addstudent(request):
	if(request.method=="POST"):
		form = forms.StudentForm(request.POST)
		if form.is_valid():
			curruser = request.user.profile.facultyid
			studentname = form.cleaned_data['studentname']
			if(Student.objects.filter(studentname=studentname)):
				print('Student exist')
				return redirect('addstudent')
			else:
				studentinput = Student(studentname=studentname, facultyid=curruser)
				studentinput.save()

			if request.POST.get("saveadd"):
				return redirect('addstudent')
			elif request.POST.get("save"):
				return redirect('student')					
	else:
		form = forms.StudentForm()

	return render(request, "teacher_student_add.html", locals())

def editstudent(request):
	if request.method=='GET':
		myid = request.GET.get('id')
		student = Student.objects.filter(studentid=myid)

	if request.method=='POST':
		myid = request.GET.get('id')
		student = Student.objects.get(studentid=myid)
		if request.POST.get("delete"):
			group = Group.objects.filter(studentid=student)
			if group:
				group.delete()
			mystudent = Student.objects.get(studentid=myid)
			mystudent.delete()
		elif request.POST.get("save"):
			students = Student.objects.filter(studentname=request.POST['studentname'])

			if students:
				for values in students:
					if student.studentname == request.POST['studentname']:
						print('Same name')
				print('Student already exist')
			else:
				student.studentname = request.POST['studentname']
				student.save()
		return redirect('student')

	return render(request, "teacher_student_edit.html", locals())

