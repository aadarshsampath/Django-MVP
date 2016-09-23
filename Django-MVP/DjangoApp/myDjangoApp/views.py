from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
	
	#This is where you do the logic that you want to appear
	#on the form.
	#For example we check if the request is POST, then we check
	# if the form is valid .
	#Then we check if there doesnt exist a full name. 
	#If thats the case we set fullname to be a name
	#ALWAYS SAVE A FORM.
	#THE VARIABLES U WANT VALUES TO APPEAR ARE IN CONTEXT.
	
	#This form relies completely on the models that was created. SignUp model.
	form = SignUpForm(request.POST or None)
	context = {
	"form" : form
	}
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "Aadarsh"

		instance.save()
		context = {
		"title":"Thankyou"
		}
	
	return render(request, "home.html", context)
