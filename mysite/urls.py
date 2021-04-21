from django.urls import path

from . import views

apps_name = 'mysite'

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login, name='login'),
    path('about.html', views.about, name='about'),
    path('job-single.html', views.jobsingle, name='jobsingle'),



]