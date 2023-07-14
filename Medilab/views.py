from django.shortcuts import render

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
