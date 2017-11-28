from django.conf.urls import url
from . import views
from django.contrib.auth import views as AuthViews
from django.contrib.auth.views import logout
from django.conf import settings
from .forms import LoginForm

urlpatterns = [
    url(r'^getArdData/$', views.getArdData, name='getArdData'),
    url(r'^saveData/$', views.saveData, name='sensData'),
    url(r'^changeStepStatus/$', views.changeStepStatus, name='changeStepStatus'),
    url(r'^$', AuthViews.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    # url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^logout/$', views.logout, name='logout'),

    # url(r'^student/$', views.student, name='student'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/members/$', views.student_members, name='student_members'),
    url(r'^home/lab_activity/$', views.lab_activity, name='lab_activity'),
    url(r'^home/labactivity/start/$', views.start, name='start'),

    # url(r'^teacher/$', views.teacher, name='teacher'),
    url(r'^home/labactivity/$', views.labactivity, name='labactivity'),
    url(r'^home/group/$', views.group, name='group'),
    url(r'^home/group/add/$', views.addgroup, name='addgroup'),
    url(r'^home/group/edit/$', views.editgroup, name='editgroup'),
    # url(r'^home/groups/labactivity/$', views.group_labactivity, name='group_labactivity'),
    url(r'^home/student/$', views.student, name='student'),
    url(r'^home/student/add/$', views.addstudent, name='addstudent'),
    url(r'^home/student/edit/$', views.editstudent, name='editstudent'),
    url(r'^home/progress/$', views.progress, name='progress'),
    url(r'^home/grade/$', views.grade, name='grade'),
    url(r'^home/grade/labactivity/$', views.grade_lab, name='grade_lab'),
]
