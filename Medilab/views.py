from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Registration, Message, Room, LiveChat, Appointment, Contact
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
def nearby_hosp(request):
    return render(request, "Medilab/nearby_hosp.html")


@login_required(login_url='/login')
def chat(request):
    return render(request, "Medilab/chat_with_us.html", {"username": request.user})


@login_required(login_url='/login')
def contact(request):
    if (request.method == 'POST'):
        user_name = request.POST.get('user_name')
        print(user_name)
        email = request.POST.get('email')
        print(email)
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contact(user_name=user_name, email=email, subject=subject, message=message)
        c.save()
        return redirect('/contact')
    else:
        return render(request, 'Medilab/contact.html')


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


@login_required(login_url='/login')
def livechat(request):
    print(request.user)
    previous_history = LiveChat.objects.filter(user=request.user)
    recent_rooms = []
    for data in previous_history:
        if (data.room not in recent_rooms):
            recent_rooms.append(data.room)
    print(recent_rooms)
    return render(request, "Medilab/livechat.html", {
        'recent_rooms': recent_rooms
    })


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


@login_required(login_url='/login')
def bmi(request):
    return render(request, "Medilab/bmi.html")


@login_required(login_url='/login')
def faq(request):
    return render(request, "Medilab/faq.html")


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'Medilab/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,

    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)


def send(request):
    values = request.POST['values']
    username = request.POST['username']
    room_id = request.POST['room_id']
    print(values, username, room_id)
    new_message = LiveChat.objects.create(values=values, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getValue(request, room):
    room_details = Room.objects.get(name=room)
    result = LiveChat.objects.filter(room=room_details.name)
    return JsonResponse({"result": list(result.values())})


@login_required(login_url='/login')
def create_appointment(request):
    if (request.method == 'POST'):
        print("hello")
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_phone_number = request.POST['user_phone_number']
        appointment_date = request.POST['appointment_date']
        doctor_name = request.POST['doctor_name']
        disease_name = request.POST['disease_name']
        user_message = request.POST['user_message']

        book_appointment = Appointment(user_name=user_name, user_email=user_email, user_phone_number=user_phone_number,
                                       appointment_date=appointment_date, doctor_name=doctor_name,
                                       disease_name=disease_name, user_message=user_message)
        book_appointment.save()
        messages.success(request, "Your appointment has been created successfully as per your request")
        return redirect('/appointment_list')
    else:
        return render(request, 'Medilab/create_appointment.html')


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'Medilab/appointment_list.html', {'appointments': appointments})
