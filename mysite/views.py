from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
            #return redirect('/')

    else:
        return render(request, 'mysite/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        #phone = request.POST['phone']
        #address = request.POST['address']
        #linkedin_id = request.POST['linkedin_id']
       # github_id = request.POST['github_id']

        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User Created!')
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching!')
            return redirect('register')
        return redirect('/')


    else:
        return render(request, 'mysite/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request, 'mysite/about.html')

def jobsingle(request):
    return render(request, 'mysite/job-single.html')

def postjob(request):
    return render(request, 'mysite/post-job.html')

def contact(request):
    return render(request, 'mysite/contact.html')

