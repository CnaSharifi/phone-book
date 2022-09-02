
from django.db.models.signals import post_save, pre_save

from .utils import slugify_contact_name

from .models import ContactModel


def contact_pre_save(sender,instance,*args, **kwargs):

    if instance.slug is None:
            slugify_contact_name(instance)

pre_save.connect(contact_pre_save,sender=ContactModel)