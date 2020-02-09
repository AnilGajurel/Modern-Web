"""SHBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app import views
urlpatterns = [
  
    path('home',views.home),
    path('signup',views.signup),
    path('entry',views.entry),
    path('userentry',views.userentry),
    path('login',views.login),
     path('adminlogin',views.adminlogin),
    path('logout',views.logout),
    path('booking',views.booking),
    path('where',views.where),
    path('register',views.register),
    path('',views.index),
    path('search',views.search),
    path('create',views.create),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('book',views.book),
    path('bookcreate',views.bookcreate),
    path('room',views.room),
    path('roomedit/<int:id>',views.roomedit),
    path('roomupdate/<int:id>',views.roomupdate),
    path('roomdelete/<int:id>',views.roomdelete),
    path('roomcreate',views.roomcreate),
    path('admindetail',views.admindetail),
    path('adminsignup',views.adminsignup),
    path('admincreate',views.admincreate),
    path('adminedit/<int:id>',views.adminedit),
    path('adminupdate/<int:id>',views.adminupdate),
    path('admindelete/<int:id>',views.admindelete),
    path('edituserdetail',views.edituserdetail),
    path('profile/<str:email>',views.profile),
    
    path('userupdate/<int:id>',views.userupdate),
    


   
]
