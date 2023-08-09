from datetime import datetime
from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Message(models.Model):
    username = models.CharField(max_length=100,null=False)
    chat_type = models.CharField(max_length=100)
    #date_time = models.DateTimeField(default=datetime.now, blank=False)
    #date = models.DateTimeField(default=datetime.now, blank=True)

    message = models.CharField(max_length=1000000)

    def __str__(self):
        return self.username

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

class LiveChat(models.Model):
    values = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class Appointment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_phone_number = models.CharField(max_length=20)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    doctor_name = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=1000)
    user_message = models.TextField(max_length=100000)

    def __str__(self):
        return self.user_name

class Contact(models.Model):
    user_name = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    subject = models.TextField(max_length=100000)
    message = models.TextField(max_length=1000000)

    def __str__(self):
        return self.user_name
