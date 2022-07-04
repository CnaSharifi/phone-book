from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ContactModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    number1 = models.CharField(max_length=15)
    number2 = models.CharField(max_length=15,null=True, blank=True)
    email = models.CharField(max_length=25,null=True, blank=True)

    

