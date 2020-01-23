from django.shortcuts import render,redirect
from app.models import User
from app.forms import UserForm
# Create your views here.
def index(request):
	return render(request,"home.html")




		

	