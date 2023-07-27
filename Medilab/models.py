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
    username = models.CharField(max_length=100)
    chat_type = models.CharField(max_length=100)
    #date_time = models.DateTimeField(default=datetime.now, blank=False)
    #date = models.DateTimeField(default=datetime.now, blank=True)

    message = models.CharField(max_length=1000000)

    def __str__(self):
        return self.username
