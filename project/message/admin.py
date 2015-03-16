from django.contrib import admin
from message.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ("messfile", "messname", "messenger", "race", "messabout", "money", "messtest",)

admin.site.register(Message, MessageAdmin)

# Register your models here.
