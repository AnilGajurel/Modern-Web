from django.db import models

# Create your models here.
class User(models.Model):
	user_id=models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=50)
	lname=models.CharField(max_length=50)
	email=models.CharField(max_length=80)
	password=models.CharField(max_length=50)
	cpassword=models.CharField(max_length=50)
	class Meta:
		db_table="user"


class Admin(models.Model):
	admin_user=models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=50)
	lname=models.CharField(max_length=50)
	email=models.CharField(max_length=80)
	password=models.CharField(max_length=50)
	cpassword=models.CharField(max_length=50)
	class Meta:
		db_table="admin"
