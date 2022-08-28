
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

from django.views.generic import View

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
            return redirect('/contacts/')
    form = AuthenticationForm(request,data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request,user)
        return redirect('/contacts/')
    context = {'form': form}
    return render(request,'accounts/login.html',context)

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    context= {'form': form}
    return render(request,'accounts/register.html',context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    context= {'user':request.user}
    return render(request,'accounts/logout.html',context)
