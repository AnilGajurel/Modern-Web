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



def home(request):
	return render(request,"home.html")

