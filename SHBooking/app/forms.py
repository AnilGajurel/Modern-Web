from django import forms
from app.models import User
from app.models import Admin, Room, Booking
class UserForm(forms.ModelForm):
	userpassword=forms.CharField(widget=forms.PasswordInput)
	usercpassword=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields="__all__"


class AdminForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	cpassword=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Admin
		fields="__all__"

class RoomForm(forms.ModelForm):
	class Meta:
		model=Room
		fields="__all__"

class BookingForm(forms.ModelForm):
	class Meta:
		model=Booking
		fields="__all__"