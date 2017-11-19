from django.conf.urls import url
from . import views
from django.contrib.auth import views as AuthViews
from django.contrib.auth.views import logout
from django.conf import settings
from .forms import LoginForm

urlpatterns = [
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
    url(r'^home/progresstracker/$', views.progresstracker, name='progresstracker'),
    url(r'^home/progresstracker/student/$', views.progresstracker_student, name='progresstracker_student')
]
