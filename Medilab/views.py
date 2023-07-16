from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Registration

# Create your views here.

def home(request):
    return render(request, "Medilab/home.html")

def services(request):
    return render(request, "Medilab/services.html")

def book_an_appointment(request):
    return render(request, "Medilab/book_an_appointment.html")

def nearby_hosp(request):
    return render(request, "Medilab/nearby_hosp.html")

def chat(request):
    return render(request, "Medilab/chat_with_us.html")

def contact(request):
    return render(request, "Medilab/contact.html")

def registration(request):
    if(request.method=='POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1==password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,"Username taken")
                return redirect('/registration')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,"Email already taken")
                return redirect('/registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                New_user = Registration(first_name=first_name, last_name=last_name, username=username, email=email, password=password1, mobile=mobile)
                New_user.save()
                user.save()
                messages.info(request,"user created")
        else:
            messages.info(request,"not matching")
            return redirect('/registration')

        return redirect('/login')
    else:
        return render(request, "Medilab/registration.html")

def login(request):
    return render(request,"Medilab/login.html")

