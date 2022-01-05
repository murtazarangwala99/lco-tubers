from django.shortcuts import render,redirect
from .models import Contactus
from django.contrib import messages
# Create your views here.
'''
def contactus(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

    contactus = Contactus(full_name=full_name,phone_number=phone_number,email=email,company_name=company_name,subject=subject,message=message)
    contactus.save()
    messages.success(request,'Thanks for reaching out!')
    return redirect('contact')

'''