from django import forms
from .models import SignUp

# Sets up the signup form accoring to how we need it.
# Class Meta helps us to assign a model to the form and extract 
# fields from that model to make the form.
class SignUpForm(forms.ModelForm):
	class Meta:
		model= SignUp
		fields = ['full_name','email']

# This is overriding the function for cleaning email data. Its named 
# as clean_email to override the default function
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base,email_prov = email.split("@")
		domain,extension = email_prov.split('.')
		if not domain=="uw":
			raise forms.ValidationError("Please use ur uw email addr")

		if not extension=="edu":
			raise forms.ValidationError("Please use a valid .edu email address")
		return email



