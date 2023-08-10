from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home",views.home ,name="home"),
    path("services", views.services, name="services"),
    path('create_appointment', views.create_appointment, name='create_appointment'),
    path('appointment_list', views.appointment_list, name='appointment_list'),
    path("nearby_hosp", views.nearby_hosp, name="nearby_hosp"),
    path("chat", views.chat, name="chat"),
    path("contact", views.contact, name="contact"),
    path("livechat", views.livechat, name="livechat"),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getValue/<str:room>/', views.getValue, name='getValue'),
    path("login", views.login, name="login"),
    path("registration", views.registration, name="registration"),
    path("logout", views.logout, name="logout"),
    path("send_message", views.send_message, name="send_message"),
    path("getMessages", views.getMessages, name="getMessages"),
    path("send_answers", views.send_answers, name="send_answers"),
    path("bmi", views.bmi, name="bmi"),
    path("faq", views.faq, name="faq"),
]
