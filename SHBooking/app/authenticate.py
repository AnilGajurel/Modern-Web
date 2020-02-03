from django.shortcuts import redirect
from app.models import User,Admin
from django.contrib import messages
from django.db.models import Q
class Authenticate:
	def valid_user(function):
		def wrap(request):
			try:
				user=User.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
				return function(request)
			except:
				messages.warning(request,'please login first')
				return redirect('/login')
		return wrap


class AdminAuthenticate:
	def valid_user(function):
		def wrap(request):
			try:
				admin=Admin.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
				return function(request)
			except:
				messages.warning(request,'invalid')
				return redirect('/adminlogin')
		return wrap