from django.contrib import admin
from .models import Registration,Message,Room,LiveChat
# Register your models here.

admin.site.register(Registration)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(LiveChat)
