from django import forms
from app.models import User
from app.models import Admin
class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	cpassword=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields="__all__"


class AdminForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	cpassword=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Admin
		fields="__all__"