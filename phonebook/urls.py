"""phonebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.decorators import login_required


from accounts.views import login_view, register_view, logout_view
from contacts.views import (home_view, search_view, detail_view, delete_view, update_view,test_view,
                            home_viewww , update_viewww, delete_viewww, detail_viewww, search_viewww)

urlpatterns = [

    #path('',Login_viewww.as_view()), 


    path('',login_view), 
    path('register/',register_view),
    path('logout/',logout_view),

    # path('contacts/',home_view),
    # path('search/',search_view),
    # path('contacts/<int:id>/',detail_view),
    # path('contacts/<int:id>/delete/',delete_view),
    # path('contacts/<int:id>/update/',update_view),

    path('contacts/', login_required(home_viewww.as_view())),
    path('contacts/<slug:slug>/update/', login_required(update_viewww.as_view())),
    path('search/', login_required(search_viewww.as_view())),
    path('contacts/<slug:slug>/', login_required(detail_viewww.as_view()), name='detail-view'),
    path('contacts/<slug:slug>/delete/', login_required(delete_viewww.as_view())),



    path('test/',test_view),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    
]
