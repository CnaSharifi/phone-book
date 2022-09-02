from django.utils.text import slugify

import random

import re


def slugify_contact_name(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():    
        random_no = random.randint(9999,99999)
        slug = f'{slug}-{random_no}'
        return slugify_contact_name(instance, new_slug = slug)
    
    instance.slug = slug
    
    return instance


        
def is_valid_mobile(mobile_string):
    mobile_regex = "^09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}$"
    if(re.search(mobile_regex, mobile_string)):
        print('true')
        return True
        
    print('false')
    return False
    
