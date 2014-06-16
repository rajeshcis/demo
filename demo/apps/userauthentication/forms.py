from django.contrib.auth.models import User
from django import forms
from userauthentication.models import Userprofile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserprofileForm(forms.ModelForm):
	"""docstring for UserprofileForm"""
	class Meta:
		model = Userprofile
		fields = ('mobileno', 'address')

