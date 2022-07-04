from django.shortcuts import render, redirect

from .models import ContactModel

from.forms import ContactFrom

from django.db.models import Q

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def home_view(request):
    form = ContactFrom(request.POST or None)
    if form.is_valid():
        #print(form.cleaned_data)
        contact_obj = ContactModel.objects.create(
        user = request.user, 
        name= form.cleaned_data['name'],
        number1 = form.cleaned_data['number1'],
        number2 = form.cleaned_data['number2'],
        email = form.cleaned_data['email'],
        )
            
    contacts_list = ContactModel.objects.filter(user = request.user)
    context = {'list':contacts_list}
    return render(request,'contacts/home.html',context)

@login_required(login_url='/')
def search_view(request):
    if request.GET == {}  or request.GET == {'q':['']} or request.GET == {'q':[' ']} :
        obj_list = None
    else:
        qs = request.GET['q']
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
def detail_view(request,id):
    obj = ContactModel.objects.get(id=id)
    context = {'obj':obj}
    return render(request,'contacts/detail.html',context)

@login_required(login_url='/')
def delete_view(request,id):
    obj = ContactModel.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/contacts/')
    context = {'obj':obj}
    return render(request,'contacts/delete.html',context)

@login_required(login_url='/')
def update_view(request,id):
    obj = ContactModel.objects.get(id=id)
    if request.method == 'GET':
        form = ContactFrom(instance=obj)
    else:
        form = ContactFrom(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/contacts/{id}/')
    context = {
    'form':form ,
    'obj': obj
    }
    return render(request,'contacts/update.html',context)
