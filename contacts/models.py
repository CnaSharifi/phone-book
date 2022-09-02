from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse



# Create your models here.
class ContactModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='کاربر')
    name = models.CharField(max_length=25,verbose_name='نام و نام خانوادگی')
    slug = models.SlugField(null=True,unique=True,blank=True,verbose_name='slug')
    number1 = models.CharField(max_length=25,verbose_name='شماره تلفن همراه')
    number2 = models.CharField(max_length=25, null=True, blank=True, verbose_name= ' شماره دوم')
    email = models.EmailField(max_length=25,null=True, blank=True,verbose_name='ایمیل')

    timestamp = models.DateField(auto_now_add=True,verbose_name='تاریخ ایجاد شدن')

    def get_absolute_url(self):
        return reverse("detail-view", kwargs={"slug": self.slug})


    def __str__(self):
        return self.name

        

    





    

    

