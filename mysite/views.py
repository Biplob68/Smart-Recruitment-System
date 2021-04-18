from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'mysite/index.html')

def login(request):
    return render(request,'mysite/login.html')

def about(request):
    return render(request,'mysite/about.html')

def jobsingle(request):
    return render(request,'mysite/job-single.html')




