from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services", views.services, name="services"),
    path("book_an_appointment", views.book_an_appointment, name="book_an_appointment"),
    path("nearby_hosp", views.nearby_hosp, name="nearby_hosp"),
    path("chat", views.chat, name="chat"),
    path("contact", views.contact, name="contact"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login",views.login,name="login"),
    path("registration",views.registration,name="registration"),
    path("logout",views.logout,name="logout"),
    path("send_message",views.send_message,name="send_message"),
    path("getMessages", views.getMessages, name="getMessages"),
    path("send_answers", views.send_answers, name="send_answers"),
]


