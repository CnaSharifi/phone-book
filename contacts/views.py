
from django.shortcuts import render, redirect

from .models import ContactModel

from.forms import ContactForm

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils import timezone


from django.urls import reverse

import random

from django.utils.crypto import get_random_string

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView


# Create your views here.


class home_viewww(CreateView,ListView):
    
    model = ContactModel
    template_name = 'contacts/home.html'
    context_object_name = 'list'
    #paginate_by = 10000

    form_class = ContactForm
    success_url = '/contacts/'
    
    def get_queryset(self):
        qs = self.model.objects.filter(user=self.request.user)
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw["user"] = self.request.user
        return kw

    

class delete_viewww(DeleteView):
    model = ContactModel
    template_name = 'contacts/delete.html'
    success_url = '/contacts/'
    context_object_name = 'obj'

class update_viewww(UpdateView):
    model = ContactModel
    template_name = 'contacts/update.html'
    form_class = ContactForm
    #success_url = '/contacts/'
    context_object_name = 'obj'

    def get_success_url(self):
        return reverse("detail-view", kwargs={"slug": self.object.slug})  

class detail_viewww(DetailView):
    model = ContactModel
    template_name = 'contacts/detail.html'
    context_object_name = 'obj'

    


class search_viewww(ListView):

    template_name = 'contacts/search.html'
    context_object_name = 'obj_list'
    model =  ContactModel
    queryset = None

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            qs = self.model.objects.filter(
            user=self.request.user).filter(
            Q(name__icontains=q)|
            Q(number1__icontains=q)|
            Q(number2__icontains=q)
            )
        else:
            qs = self.model.objects.none()

        return qs
            

    

@login_required(login_url='/')
def home_view(request):
    form = ContactForm(request.POST or None, user=request.user)
    if form.is_valid():
        #print(request.user)
        form.save()
        
    contacts_list = ContactModel.objects.filter(user = request.user)
    context = {
        'list':contacts_list,
        'form': form}

    return render(request,'contacts/home.html',context)

@login_required(login_url='/')
def search_view(request):
   
    print(request.GET.get('q'))

    if request.GET == {}  or request.GET.get('q','').strip() == '':
        obj_list = None
    else:
        qs = request.GET.get('q')
        #print(qs)

        obj_list =  ContactModel.objects.filter(
        user=request.user).filter(
        Q(name__icontains=qs)|
        Q(number1__icontains=qs)|
        Q(number2__icontains=qs)
        )
        # print(obj_list)
    context = {'obj_list': obj_list}
    return render(request,'contacts/search.html',context)

@login_required(login_url='/')
def detail_view(request,slug):
    obj = ContactModel.objects.get(slug=slug)
    context = {'obj':obj}
    return render(request,'contacts/detail.html',context)



@login_required(login_url='/')
def delete_view(request,slug):
    obj = ContactModel.objects.get(slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/contacts/')
    context = {'obj':obj}
    return render(request,'contacts/delete.html',context)



@login_required(login_url='/')
def update_view(request,slug):
    obj = ContactModel.objects.get(slug=slug)
    if request.method == 'GET':
        form = ContactForm(instance=obj)
    else:
        form = ContactForm(request.POST,instance=obj) 
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()

            return redirect(f'/contacts/{slug}/')
    context = {
    'form':form ,
    'obj': obj
    }
    return render(request,'contacts/update.html',context)


def test_view(request):
    import redis
    r = redis.Redis(host='localhost', port=6379, db=0)
    res = r.get('name').decode()
    print(res)


    return render(request,'contacts/home.html')