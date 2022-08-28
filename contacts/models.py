from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

from django.db.models.signals import post_save, pre_save

from .utils import slugify_contact_name



# Create your models here.
class ContactModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    slug = models.SlugField(null=True,unique=True)
    number1 = models.CharField(max_length=25)
    number2 = models.CharField(max_length=25, null=True, blank=True)
    email = models.CharField(max_length=25,null=True, blank=True)

    timestamp = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("detail-view", kwargs={"slug": self.slug})


    def __str__(self):
        return self.name

        

    

def contact_pre_save(sender,instance,*args, **kwargs):

    if instance.slug is None:
            slugify_contact_name(instance)

pre_save.connect(contact_pre_save,sender=ContactModel)



    

    

