from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')

def login(request):
    return render(request, 'mysite/login1.html')

def about(request):
    return render(request, 'mysite/about.html')

def jobsingle(request):
    return render(request, 'mysite/job-single.html')

def postjob(request):
    return render(request, 'mysite/post-job.html')

def contact(request):
    return render(request, 'mysite/base.html')

