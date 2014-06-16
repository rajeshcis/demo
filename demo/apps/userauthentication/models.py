from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userprofile(models.Model):
	"""docstring for Userprofile"""
	user = models.OneToOneField(User)
	mobileno = models.CharField(max_length='20')
	address = models.CharField(max_length='250')

	def __unicode__(self):
		return self.user.username

