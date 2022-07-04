from django.forms import ModelForm

from .models import ContactModel

class ContactFrom(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'number1', 'number2', 'email']
        