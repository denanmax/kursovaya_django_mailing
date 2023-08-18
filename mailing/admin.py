from django.contrib import admin

from mailing.models import Customer, Message, Sender


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'middle_name', 'email')
    list_filter = ('surname', 'email')

@admin.register(Message)
class MessgaeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message', 'is_active')
    list_filter = ('subject',)

@admin.register(Sender)
class SenderAdmin(admin.ModelAdmin):
    list_display = ('commence_time', 'frequency', 'status', 'message',)

