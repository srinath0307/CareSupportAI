from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services", views.services, name="services"),
    path("book_an_appointment", views.book_an_appointment, name="book_an_appointment"),
    path("nearby_hosp", views.nearby_hosp, name="nearby_hosp"),
    path("chat", views.chat, name="chat"),
    path("contact", views.contact, name="contact"),
]

