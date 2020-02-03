from django.shortcuts import render,redirect
from app.models import User, Admin
from app.forms import UserForm, AdminForm
from django.http import HttpResponse,JsonResponse
from app.authenticate import Authenticate, AdminAuthenticate
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.
def layout(request):
	return render(request,'layout.html')


def login(request):
	return render(request,"login.html")

def adminlogin(request):
	return render(request,"adminlogin.html")


def home(request):
	return render(request,"home.html")

def signup(request):
	return render(request,"signup.html")

def booking(request):
	return render(request,"booking.html")

def where(request):
	return render(request,"where.html")

def register(request):
	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
	else:
		form=UserForm()
	return render(request,'signup.html',{'form':form})



def layout2(request):
	return render(request,'layout2.html')

def entry(request):
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect('/admindetail')



def logout(request):
    auth.logout(request)
    return redirect('/login')

@AdminAuthenticate.valid_user
def index(request):
	limit=5
	page=1
	if request.method=="POST":
		if "next" in request.POST:
			page=(int(request.POST['page'])+1)
		elif "prev" in request.POST:
			page=(int(request.POST['page'])-1)
		tempoffset=page-1
		offset=tempoffset*page
		users=User.objects.raw("select * from user limit 5 offset %s",[offset])
	else:
		users=User.objects.raw("select * from user limit 5 offset 0")
	return render(request,"index.html",{'users':users,'page':page})

def search(request):
	users=User.objects.filter(email__contains=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)

def create(request):
	if request.method=="POST":
		form=UserForm(request.POST)
		form.save()
		return redirect('/')
	form=UserForm()
	return render(request,'create.html',{'form':form})

def edit(request,id):
	user=User.objects.get(user_id=id)
	return render(request,'edit.html',{'user':user})

def update(request,id):
	user=User.objects.get(user_id=id)
	form=UserForm(request.POST,instance=user)
	form.save()
	return redirect('/')

def delete(request,id):
	user=User.objects.get(user_id=id)
	user.delete()
	return redirect('/')

@AdminAuthenticate.valid_user
def book(request):
	return render(request,"book.html")

@AdminAuthenticate.valid_user
def room(request):
	return render(request,"room.html")

@AdminAuthenticate.valid_user
def admindetail(request):
	admins=Admin.objects.all()
	return render(request,"admindetail.html",{'admins':admins})


def adminsignup(request):
	return render(request,"adminsignup.html")


def admincreate(request):
	if request.method=="POST":
		form=AdminForm(request.POST)
		form.save()
		return redirect('/admindetail')
	form=AdminForm()
	return render(request,'adminsignup.html',{'form':form})


def adminedit(request,id):
	admin=Admin.objects.get(admin_user=id)
	return render(request,'adminedit.html',{'admin':admin})

def adminupdate(request,id):
	admin=Admin.objects.get(admin_user=id)
	form=AdminForm(request.POST,instance=admin)
	form.save()
	return redirect('/admindetail')

def update(request,id):
	user=User.objects.get(user_id=id)
	form=UserForm(request.POST,instance=user)
	form.save()
	return redirect('/')

def admindelete(request,id):
	admin=Admin.objects.get(admin_user=id)
	admin.delete()
	return redirect('/admindetail')