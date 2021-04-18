from django.urls import path

from . import views

apps_name = 'mysite'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('jobsingle', views.jobsingle, name='jobsingle'),



]