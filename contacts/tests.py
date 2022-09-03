
from unicodedata import name
from .models import ContactModel

from .forms import ContactForm

from django.contrib.auth import get_user_model

User = get_user_model()

from django.test import TestCase
# Create your tests here.
class ContactsTestCase(TestCase):

    def setUp(self):
        self.model = ContactModel
        self.form = ContactForm
        self.data = {'name': 'Andro==@#$%*()==سلام', 'number1': '09132272599', 'number2': '3136681313', 'email': 'Andro.qwerty@gmail.com'}
        self.user = User.objects.create(username='user_test')
        self.user.set_password('12345')
        self.user.save()


    def test_create_contact_form(self):
        """check when submit create contact form, a contact in database is registered"""
        self.assertEqual(self.model.objects.count(), 0) # Check that our ContactModel table is empty
        
        form = self.form(self.data,user=self.user) 
        form.save()   # form sumbit !!!
        contact_obj = self.model.objects.first() # getting the first object from ContactModel

        self.assertEqual(self.model.objects.count(), 1)   # a contact in db is registered

        """checking that the data in database are the same as the form"""
        self.assertEqual(contact_obj.name, self.data['name'])
        self.assertEqual(contact_obj.number1, self.data['number1'])
        self.assertEqual(contact_obj.number2, self.data['number2'])
        self.assertEqual(contact_obj.email, self.data['email'])
        self.assertEqual(contact_obj.user, self.user)



    def test_create_contact_form_validation(self):
        # creating a sample contact with a certain name
        contact_name = 'david'
        self.model.objects.create(name= contact_name,number1='09121141718',user = self.user)
        self.assertEqual(self.model.objects.count(), 1)
        # creating a form with the same name to check if it validates
        data = {'name': contact_name, 'number1': '09215690594', 'number2': '8777', 'email': 'sin4.sh@gmail.com'}
        form = self.form(data,user= self.user)
        # name should be unique so form should not be valid
        if form.is_valid():
            print('Unique name validation is NOT working true')
            self.assertFalse(True)
        
        self.model.objects.get(name=contact_name).delete() # now table is empty

        """testing REGEX --- phone number validation"""
        wrong_number='09652245687' # wrong pre number --- 0965 !!!
        data['number1'] = wrong_number
        form = self.form(data, user= self.user)
        if form.is_valid():
            print(wrong_number , 'REGEX is NOT working true')
            self.assertFalse(True)
        
        wrong_number='0913777588' # 10 characters --- should be 11
        data['number1'] = wrong_number
        form = self.form(data, user= self.user)
        if form.is_valid():
            print(wrong_number , 'REGEX is NOT working true')
            self.assertFalse(True)

        wrong_number='09137s75882' # contains alphabet 's'
        data['number1'] = wrong_number
        form = self.form(data, user= self.user)
        if form.is_valid():
            print(wrong_number , 'REGEX is NOT working true')
            self.assertFalse(True)

        self.assertEqual(self.model.objects.count(), 0) # no objects is created !



    def test_delete_contact_form_view(self):
        
        contact_obj = self.model.objects.create(name='farhad',number1='09137985566',user=self.user) # 1 contact created
        self.client.login(username='user_test', password='12345') #login
        
        response = self.client.get(f"/contacts/{contact_obj.slug}/delete/") # get the delete view
        self.assertEqual(response.status_code, 200)  # check 200 OK response

        self.assertEqual(self.model.objects.count(), 1) # check that we have one object before delete !
        response = self.client.post(f"/contacts/{contact_obj.slug}/delete/") # form submited
        self.assertEqual(response.status_code, 302)  # check 302 OK --- 302 is for redirect so its true
        """check that obj does not exists"""
        qs = self.model.objects.filter(slug=contact_obj.slug) 
        if qs.exists():
            self.assertFalse(True)

        self.assertEqual(self.model.objects.count(), 0) # after form submit [deleted] it should be 0 !
        




    def test_update_contact_form(self):

        contact_obj = self.model.objects.create(name= 'alireza',number1='09139999999',user = self.user)
        
        self.assertTrue(contact_obj == self.model.objects.first()) # contact is created

        form = self.form(self.data,instance=contact_obj)
        form.save() # update saved

        contact_obj = self.model.objects.first()
        """checking that update done or not"""
        self.assertEqual(contact_obj.name, self.data['name'])
        self.assertEqual(contact_obj.number1, self.data['number1'])
        self.assertEqual(contact_obj.number2, self.data['number2'])
        self.assertEqual(contact_obj.email, self.data['email'])
        self.assertEqual(contact_obj.user, self.user)


    def test_update_contact_form_view(self):

        contact_obj = self.model.objects.create(name='farhad',number1='09137985566',user=self.user) # 1 contact created
        self.client.login(username='user_test', password='12345') #login
        
        response = self.client.get(f"/contacts/{contact_obj.slug}/update/") # get the delete view
        self.assertEqual(response.status_code, 200)  # check 200 OK response
    
        response = self.client.post(f"/contacts/{contact_obj.slug}/update/",data=self.data) # update form submited
        self.assertEqual(response.status_code, 302)  # check 302 OK --- 302 is for redirect so its true
        contact_obj = self.model.objects.first()
        """checking that update is done"""
        self.assertEqual(contact_obj.name, self.data['name'])
        self.assertEqual(contact_obj.number1, self.data['number1'])
        self.assertEqual(contact_obj.number2, self.data['number2'])
        self.assertEqual(contact_obj.email, self.data['email'])
        self.assertEqual(contact_obj.user, self.user)


        

    def test_contacts_list_view(self):
        """
        Write a unit test to get list of contacts, for example create multiple contacts,
         then call list of contacts page and check if contacts are created and count match
        """
        logged_in = self.client.login(username='user_test', password='12345')
        self.assertTrue(logged_in)
        self.assertEqual(self.model.objects.count(), 0) 
        
        import random
        for i in range(100):
            self.model.objects.create(
                name= f'john{i}',
                number1= f'0912{random.randint(111111,999999)}',
                user=self.user
            )    

        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)  # check 200 OK response
        contacts_list = response.context['list'] 
        
        self.assertEqual(contacts_list.count(),100) # so its OK


        
        
        

            
        

    
