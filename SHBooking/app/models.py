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

class Room(models.Model):
	room_id=models.AutoField(auto_created=True,primary_key=True)
	roomname=models.CharField(max_length=100)
	image=models.ImageField(default='img.jpg')
	description=models.CharField(max_length=100)
	price=models.FloatField()
	class Meta:
		db_table="room"