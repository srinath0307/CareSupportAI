from django.contrib import admin
from .models import Registration,Message,Room,LiveChat,Appointment,Contact
# Register your models here.

admin.site.register(Registration)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(LiveChat)
admin.site.register(Appointment)
admin.site.register(Contact)

