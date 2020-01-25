from django.shortcuts import redirect
from app.models import User
from django.contrib import messages
class Authenticate:
	def valid_user(function):
		def wrap(request):
			try:
				User.objects.get(email=request.session['email'])
				return function(request)
			except:
				messages.warning(request,'please login first')
				return redirect('login')
		return wrap