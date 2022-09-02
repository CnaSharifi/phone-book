from django.contrib import admin

from .models import ContactModel
# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'number1','number2','email','timestamp']
    search_fields = ['name', 'number1','number2']

admin.site.register(ContactModel, ContactModelAdmin)
