from django.urls import path

from . import views

#apps_name = 'mysite'

urlpatterns = [
    path("", views.index, name="home"),
    path("login.html", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name ="logout"),
    path("about/", views.about, name="about"),
    path("job-single.html", views.jobsingle, name="jobsingle"),
    path("post-job.html", views.postjob, name="jobsingle"),
    path("contact/", views.contact, name="contact"),


]