from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, username, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not username:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')

		user = self.create_user(email, password)
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user


class AppUser(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	username = models.CharField(max_length=50)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	objects = AppUserManager()
	def __str__(self):
		return self.username

class Package(models.Model):
	pack_id = models.AutoField(primary_key=True)
	sender = models.CharField(max_length=100)
	receiver = models.CharField(max_length=100)
	name = models.CharField(max_length=100) 
	description = models.CharField(max_length=300)
	sender_city = models.CharField(max_length=100)
	destination_city = models.CharField(max_length=100)
	tracking = models.BooleanField(default=False)
	status = models.CharField(max_length=100)