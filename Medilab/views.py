from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Registration, Message
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Medilab.dataset.chatbot import calling, final_count
from datetime import datetime


# Create your views here.

def home(request):
    return render(request, "Medilab/home.html")


@login_required(login_url='/login')
def services(request):
    return render(request, "Medilab/services.html")


@login_required(login_url='/login')
def book_an_appointment(request):
    return render(request, "Medilab/book_an_appointment.html")


@login_required(login_url='/login')
def nearby_hosp(request):
    return render(request, "Medilab/nearby_hosp.html")


@login_required(login_url='/login')
def chat(request):
    return render(request, "Medilab/chat_with_us.html", {"username": request.user})


@login_required(login_url='/login')
def contact(request):
    return render(request, "Medilab/contact.html")


def registration(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if (password1 == password2):
            if (User.objects.filter(username=username).exists()):
                messages.warning(request, "Username already taken")
                return redirect('/registration')
            elif (User.objects.filter(email=email).exists()):
                messages.warning(request, "Email already taken")
                return redirect('/registration')
            elif (Registration.objects.filter(mobile=mobile).exists()):
                messages.warning(request, "Mobile number already taken")
                return redirect('/registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                New_user = Registration(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password1, mobile=mobile)
                New_user.save()
                user.save()
                messages.success(request, "Your account has been created successfully")
        else:
            messages.warning(request, "Passwords not matching")
            return redirect('/registration')

        return redirect('/login')
    else:
        return render(request, "Medilab/registration.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('/login')
    else:
        return render(request, "Medilab/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def dashboard(request):
    return render(request, "Medilab/dashboard.html")


def send_message(request):
    li = ["what are you experiencing", "for how many days", "searches related to input"]
    answers = ["I am experiencing fever", "for 2 days", "fever,headache,weakness"]
    if request.method == 'POST':
        username = request.user
        message = request.POST['message']
        chat_messages = Message(username=username, chat_type="user", message=message)
        chat_messages.save()
        return JsonResponse({"message": "success"})


def send_answers(request):
    if request.method == 'POST':
        username = request.user
        message = request.POST['message_0']
        message1 = request.POST['message_1']
        message2 = request.POST['message_2']
        present_disease, symptoms_given, description, precaution = calling(message, int(message1), int(message2))
        symptoms_given = list(symptoms_given)
        print(present_disease, list(symptoms_given))
        # chat_messages = Message(username=username, chat_type="user", message=message)
        # chat_messages.save()
        return JsonResponse(
            {"present_disease": present_disease, "symptoms_given": symptoms_given, "description": description,
             "precaution": precaution})


def getMessages(request):
    chat_details = Message.objects.filter(username=request.user)
    text = []
    # l = cringe()
    # print(l)
    for message in chat_details:
        text.append([message.message, message.chat_type])
    # count = retCount()
    # text[0].append(l[-1])

    return JsonResponse({"messages": text})
