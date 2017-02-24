from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm


def contact(request):
	title='Contact Me'
	form=contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		Name=form.cleaned_data['Name']
		Comment = form.cleaned_data['Comment']
		subject = "Message from ur contact app"
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]


		send_mail(subject ,Comment,emailFrom,emailTo ,fail_silently=True)
		title = "Thanks !"
		confirm_message = "Thanks for your response"
		form=None

	context = {'title': title, 'form':form, 'confirm_message': confirm_message,} 
	
	template = 'contact.html'
	return render(request,template,context)
