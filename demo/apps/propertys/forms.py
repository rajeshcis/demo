from django.forms import ModelForm

class PropertyForm(ModelForm):
	"""docstring for PropertyForm"""
	def __init__(self, arg):
		super(PropertyForm, self).__init__()
		self.arg = arg
