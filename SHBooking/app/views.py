from django.shortcuts import render,redirect
from app.models import User, Admin, Room, Booking
from app.forms import UserForm, AdminForm, RoomForm, BookingForm
from django.http import HttpResponse,JsonResponse
from app.authenticate import Authenticate, AdminAuthenticate
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.
def layout(request):
	users=User.objects.all()
	return render(request,'layout.html',{'users':users})


def login(request):
	return render(request,'login.html')
	# if 'useremail' not in request.session:
	# 	return render(request,'login.html')
	# else:
	# 	return render(request,"home.html")

def adminlogin(request):
	return render(request,"adminlogin.html")


def home(request):
	rooms=Room.objects.all()
	return render(request,"home.html",{'rooms':rooms})

def signup(request):
	return render(request,"signup.html")



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

def userentry(request):
	request.session['useremail']=request.POST['useremail']
	request.session['userpassword']=request.POST['userpassword']
	return redirect('/booking')

def layout2(request):
	return render(request,'layout2.html')

def entry(request):
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect('/admindetail')

def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('/adminlogin')

def logoutuser(request):
    del request.session['useremail']
    del request.session['userpassword']
    return redirect('/home')

@AdminAuthenticate.valid_user
def index(request):
	limit=3
	page=1
	if request.method=="POST":
		if "next" in request.POST:
			page=(int(request.POST['page'])+1)
		elif "prev" in request.POST:
			page=(int(request.POST['page'])-1)
		tempoffset=page-1
		offset=tempoffset*page
		users=User.objects.raw("select * from user limit 3 offset %s",[offset])
	else:
		users=User.objects.raw("select * from user limit 3 offset 0")
	return render(request,"index.html",{'users':users,'page':page})

def search(request):
	users=User.objects.filter(useremail__contains=request.GET['search'])[0:3].values()
	return JsonResponse(list(users),safe=False)

def adminsearch(request):
	admins=Admin.objects.filter(email__contains=request.GET['search'])[0:3].values()
	return JsonResponse(list(admins),safe=False)


def roomsearch(request):
	rooms=Room.objects.filter(roomname__contains=request.GET['search']).values()
	return JsonResponse(list(rooms),safe=False)

def booksearch(request):
	books=Booking.objects.filter(Fname__contains=request.GET['search']).values()
	return JsonResponse(list(books),safe=False)




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


	
def room(request):
	rooms=Room.objects.all()
	return render(request,"room.html",{'rooms':rooms})

def roomcreate(request):
	if request.method=="POST":
		form=RoomForm(request.POST,request.FILES)
		form.save()
		return redirect('/room')
	form=RoomForm()
	return render(request,'roomcreate.html',{'form':form})

def roomedit(request,id):
	room=Room.objects.get(room_id=id)
	return render(request,'roomedit.html',{'room':room})

def roomupdate(request,id):
	room=Room.objects.get(room_id=id)
	form=RoomForm(request.POST,request.FILES,instance=room)
	form.save()
	return redirect('/room')


def roomdelete(request,id):
	room=Room.objects.get(room_id=id).image.delete()
	room=Room.objects.get(room_id=id)
	room.delete()
	return redirect('/room')

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


def admindelete(request,id):
	admin=Admin.objects.get(admin_user=id)
	admin.delete()
	return redirect('/admindetail')

def edituserdetail(request,id):
	user=User.objects.get(user_id=id)
	return render(request,'edituserdetail.html',{'user':user})



def userupdate(request,user_id):
	user=User.objects.get(user_id=user_id)
	form=UserForm(request.POST,instance=user)
	form.save()
	return redirect('/home')


def profile(request,useremail="request.session.useremail"):
	user=User.objects.get(useremail=useremail)
	return render(request,"profile.html",{'user':user})


@Authenticate.valid_user
def booking(request):
	return render(request,"booking.html")

def Bookform(request):
	if request.method=="POST":
		form=BookingForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')
	else:
		form=BookingForm()
	return render(request,'booking.html',{'form':form})



@AdminAuthenticate.valid_user
def book(request):
	limit=3
	page=1
	if request.method=="POST":
		if "next" in request.POST:
			page=(int(request.POST['page'])+1)
		elif "prev" in request.POST:
			page=(int(request.POST['page'])-1)
		tempoffset=page-1
		offset=tempoffset*page
		books=Booking.objects.raw("select * from booking limit 3 offset %s",[offset])
	else:
		books=Booking.objects.raw("select * from booking limit 3 offset 0")
	return render(request,"book.html",{'books':books,'page':page})

