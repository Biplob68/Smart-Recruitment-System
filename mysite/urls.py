from django.urls import path, include
from django.contrib import admin
from . import views


# Django Admin header Customization
admin.site.site_header = "Login for admin dashboard"
#apps_name = 'mysite'

urlpatterns = [
    path('', views.index, name="index"),
    path("login.html", views.login, name="login"),
    path("register.html", views.register, name="register"),
    path("logout.html", views.logout, name ="logout"),
    path("about.html", views.about, name="about"),
    path("job_listing.html", views.job_listing, name="job_listing"),
    path("post-job.html", views.postjob, name="postjob"),
    path("contact.html", views.contact, name="contact"),



]