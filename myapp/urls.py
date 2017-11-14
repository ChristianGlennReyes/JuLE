from django.conf.urls import url
from . import views
from django.contrib.auth import views as AuthViews
from django.contrib.auth.views import logout
from django.conf import settings
from .forms import LoginForm

urlpatterns = [
    url(r'^$', AuthViews.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    # url(r'^student/$', views.student, name='student'),
    url(r'^home/$', views.home, name='home'),
    url(r'^student/members/$', views.student_members, name='student_members'),
    url(r'^student/labactivity/$', views.lab_activity, name='lab_activity'),
    url(r'^student/labactivity/start/$', views.start, name='start'),
    # url(r'^teacher/$', views.teacher, name='teacher'),
    url(r'^teacher/labactivity/$', views.labactivity, name='labactivity'),
    url(r'^teacher/progresstracker/$', views.progresstracker, name='progresstracker'),
    url(r'^teacher/progresstracker/student/$', views.progresstracker_student, name='progresstracker_student')
]
