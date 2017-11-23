from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.Faculty)
admin.site.register(models.Student)
admin.site.register(models.StudentGroup)
admin.site.register(models.Group)
# admin.site.register(models.Grade)
admin.site.register(models.Sensors)
admin.site.register(models.LabActivity)
admin.site.register(models.LabProcedure)
admin.site.register(models.GroupGrade)
admin.site.register(models.DataValue)
# admin.site.register(models.LabProcedureStatus)