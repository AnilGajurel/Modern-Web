from django.shortcuts import render,redirect
from app.models import User
from app.forms import UserForm
from django.http import HttpResponse,JsonResponse
from app.authenticate import Authenticate 
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.
def layout(request):
	return render(request,'layout.html')


def login(request):
	return render(request,"login.html")

def home(request):
	return render(request,"home.html")


def signup(request):
	return render(request,"signup.html")

def booking(request):
	return render(request,"booking.html")

def register(request):
	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
	else:
		form=UserForm()
	return render(request,'signup.html',{'form':form})







