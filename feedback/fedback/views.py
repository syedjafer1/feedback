from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import fb



def index(request):
	if(request.method == 'POST'):
		Name = request.POST['Name']
		Department = request.POST['Department']
		Comment = request.POST['Comment']
		feed = fb(Name=Name , Department=Department ,Comment=Comment)
		feed.save()
		title = "THANKS !"
		confirm_message = "Thanks for the message . We Will get right back to you."
		context = {'confirm_message': confirm_message,} 
		return render(request,'index.html',context)
	#	return redirect("/")

	else:
		return render(request, 'index.html')


# Create your views here.
