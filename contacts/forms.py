from django.forms import ModelForm

from .models import ContactModel

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'number1', 'number2', 'email']
    
    def __init__(self,*args, **kwargs):
        #timestamp = kwargs.pop("timestamp",None)
        user = kwargs.pop("user",None)
        super().__init__(*args, **kwargs)
        if not self.instance.id:
            self.instance.user = user
            #self.instance.timestamp = timestamp
    
    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data['name']
        qs = ContactModel.objects.filter(name__iexact = name).exclude(id=self.instance.id)

        if qs.exists():
            self.add_error('name','this name already exists ! ')

        
        number1 = cleaned_data.get('number1')

        #print(number1)
        if number1.startswith('913'):
            pass
        else:
            self.add_error('number1','phone number should start with 913 !!!')
      
        
        return cleaned_data
    

    
            