from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
	facultyid = models.IntegerField(primary_key=True)
	facultyname = models.CharField(max_length=80)

	def __str__(self):
		return self.facultyname

class Student(models.Model):
	studentid = models.IntegerField(primary_key=True)
	studentname = models.CharField(max_length=80, blank=True, null=True)
	facultyid = models.ForeignKey(Faculty, models.DO_NOTHING)

	def __str__(self):
		return self.studentname

class StudentGroup(models.Model):
	groupid = models.IntegerField(primary_key=True)
	facultyid = models.ForeignKey(Faculty, models.DO_NOTHING)
	groupname = models.CharField(max_length=45, blank=True, null=True)

	def __str__(self):
		return self.groupname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.BooleanField()
    facultyid = models.ForeignKey(Faculty, models.DO_NOTHING, blank=True, null=True)
    groupid = models.ForeignKey(StudentGroup, models.DO_NOTHING, blank=True, null=True)
    loggedin = models.BooleanField()

    def __str__(self):
    	return self.user.username

class Group(models.Model):
	groupid = models.ForeignKey(StudentGroup, models.DO_NOTHING)
	studentid = models.ForeignKey(Student, models.DO_NOTHING)

	def __str__(self):
		return str(self.groupid) + " - " + str(self.studentid)

class Grade(models.Model):
	gradeid = models.FloatField(primary_key=True)
	grademin = models.IntegerField(blank=True, null=True)
	grademax = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.gradeid)

class Sensors(models.Model):
	sensorid = models.IntegerField(primary_key=True)
	sensorname = models.CharField(unique=True, max_length=100)

	def __str__(self):
		return self.sensorname

class LabActivity(models.Model):
	labid = models.IntegerField(primary_key=True)
	labname = models.CharField(unique=True, max_length=100)
	labsummary = models.TextField(blank=True, null=True)
	numprocedures = models.IntegerField()
	hidden = models.BooleanField()
	selected = models.BooleanField()

	def __str__(self):
		return self.labname

class LabProcedure(models.Model):
	procedureid = models.IntegerField(primary_key=True)
	labid = models.ForeignKey(LabActivity, models.DO_NOTHING)
	sensorid = models.ForeignKey(Sensors, models.DO_NOTHING, blank=True, null=True)
	stepnum = models.IntegerField()
	procedurename = models.CharField(max_length=100, null=False)
	proceduredesc = models.TextField()
	minvalue = models.IntegerField(blank=True, null=True)
	maxvalue = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.labid) + " - " + str(self.procedurename)

class GroupGrade(models.Model):
	groupid = models.ForeignKey(StudentGroup, models.DO_NOTHING)
	procedureid = models.ForeignKey(LabProcedure, models.DO_NOTHING)
	gradeid = models.ForeignKey(Grade, models.DO_NOTHING)

	def __str__(self):
		return str(self.groupid) + " - " + str(self.procedureid) + " - " + str(self.gradeid)

class DataValue(models.Model):
	procedureid = models.ForeignKey(LabProcedure, models.DO_NOTHING)
	groupid = models.ForeignKey(StudentGroup, models.DO_NOTHING)
	value = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.procedureid) + " - " + str(self.groupid) + " - " + str(self.value)

class LabProcedureStatus(models.Model):
	groupid = models.ForeignKey(StudentGroup, models.DO_NOTHING)
	procedureid = models.ForeignKey(LabProcedure, models.DO_NOTHING)
	status = models.BooleanField()

	def __str__(self):
		return str(self.groupid) + " - " + str(self.procedureid) + " - " + str(self.status)