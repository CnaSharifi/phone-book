
from .models import ContactModel

from .forms import ContactForm

from django.contrib.auth import get_user_model

User = get_user_model()

from django.test import TestCase
# Create your tests here.
class ContactsTestCase(TestCase):

    def setUp(self):
        """ in the setup function we can define variables that we will need in our tests """
        self.data = {'name': 'sina', 'number1': '91321212', 'number2': '3136681313', 'email': 'sin4.sh@gmail.com'}
        """create a simple user for test """
        self.user = User.objects.create(username='user_test')
        self.user.set_password('12345')
        self.user.save()


    def test_contact_creation_by_form_sumbit(self):
        """check when submit create contact form, a contact in database is registered"""
        self.assertEqual(ContactModel.objects.count(), 0) # Check that our ContactModel table is empty
        
        form = ContactForm(self.data,user=self.user) 
        form.save()   # form sumbit !!!
        obj = ContactModel.objects.first() # getting the first object from ContactModel

        self.assertEqual(ContactModel.objects.count(), 1)   # a contact in db is registered

        """checking that the data in database are the same as the form"""
        self.assertEqual(obj.name, self.data['name'])
        self.assertEqual(obj.number1, self.data['number1'])
        self.assertEqual(obj.number2, self.data['number2'])
        self.assertEqual(obj.email, self.data['email'])
        self.assertEqual(obj.user, self.user)





    def test_contacts_list_view(self):
        """
        Write a unit test to get list of contacts, for example create multiple contacts,
         then call list of contacts page and check if contacts are created and count match
        """
        logged_in = self.client.login(username='user_test', password='12345')
        self.assertTrue(logged_in)
        
        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)  # check 200 OK response
        self.assertEqual(ContactModel.objects.count(), 0) 

        import random
        for i in range(100):
            ContactModel.objects.create(
                name= f'john{i}',
                number1= f'913{random.randint(111111,999999)}',
                user=self.user
            )    

        response = self.client.get("/contacts/")
        contacts_list = response.context['list']
        
        self.assertEqual(contacts_list.count(),100)



    def test_create_and_update_contact(self):

        self.assertEqual(ContactModel.objects.count(), 0) # 0 contact is DB

        obj = ContactModel.objects.create(name= 'ali',number1='09139999999',user = self.user)
        #print(obj.name, obj.number1, obj.email)
        
        self.assertTrue(obj == ContactModel.objects.first()) # contact is created

        form = ContactForm(self.data,instance=obj)
        form.save() # update saved
        #print(obj.name, obj.number1, obj.email)

        obj = ContactModel.objects.first()

        self.assertEqual(obj.name, self.data['name'])
        self.assertEqual(obj.number1, self.data['number1'])





    def test_form_validation(self):
        ContactModel.objects.create(name= 'sina',number1='0935626012',user = self.user)
        data_test_name = {'name': 'sina', 'number1': '9131313', 'number2': '8777', 'email': 'sin4.sh@gmail.com'}
        form = ContactForm(data_test_name,user= self.user)
        #print(form.is_valid())
        if form.is_valid():
            print('form validation is NOT working true')
            self.assertTrue(False)

        data_test_number = {'name': 'john', 'number1': '09101313', 'number2': '13131313', 'email': 'sin4.sh@gmail.com'}
        form = ContactForm(data_test_number, user= self.user)
        #print(form.is_valid())
        if form.is_valid():
            print('form validation is NOT working true')
            self.assertTrue(False)

        

            
        

    
