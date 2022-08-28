from operator import contains
from django.core.management.base import BaseCommand
from contacts.models import ContactModel

import time

class Command(BaseCommand):
    help = 'Delete all the contacts !'

    def handle(self, *args, **kwargs):
        qs = ContactModel.objects.all()
        st = time.time()
        for i in qs :
            i.delete()

        et = time.time()
        print(et-st)


    
        