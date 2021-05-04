from django.urls import path

from . import views

#apps_name = 'mysite'

urlpatterns = [
    path("", views.index, name="index"),
    path("login.html", views.login, name="login"),
    path("register.html", views.register, name="register"),
    path("logout.html", views.logout, name ="logout"),
    path("about.html", views.about, name="about"),
    path("job-single.html", views.jobsingle, name="jobsingle"),
    path("post-job.html", views.postjob, name="postjob"),
    path("contact.html", views.contact, name="contact"),


]