from django.contrib.auth.models import User
from contacts.models import ContactModel
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

import random
import time

class Command(BaseCommand):
    help = 'Create contacts'

    def add_arguments(self, parser):
        parser.add_argument('number_of_contacts', type=int, help='Indicates the number of contacts to be created')

    # def handle(self, *args, **kwargs):
    #     number_of_contacts = kwargs['number_of_contacts']
    #     st = time.time()
    #     for i in range(number_of_contacts):
    #         #User.objects.create_user(username=get_random_string(), email='', password='123')
    #         ContactModel.objects.create(name=get_random_string(8),number1=f'913{random.randint(111111,999999)}',user=User.objects.get(id=1))
    #     et = time.time()
    #     print(et-st)
    
    def handle(self, *args, **kwargs):
        number_of_contacts = kwargs['number_of_contacts']
        st = time.time()
        list_test=[]
        for i in range(number_of_contacts):
            #User.objects.create_user(username=get_random_string(), email='', password='123')
            list_test.append(
            ContactModel(name=get_random_string(8),number1=f'913{random.randint(111111,999999)}',user_id=1)
            )
        ContactModel.objects.bulk_create(list_test)
        et = time.time()
        print(et-st)