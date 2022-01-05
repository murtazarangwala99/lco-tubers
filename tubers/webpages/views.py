from django.shortcuts import render,redirect
from .models import Slider, Team, About
from contactus.models import Contactus
from youtubers.models import Youtuber
from django.contrib import messages

# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders' : sliders,
        'teams': teams,
        'featured_youtubers':featured_youtubers,
        'all_tubers':all_tubers,
        
    } 
    return render(request,'webpages/home.html',data)
def about(request):
    teams = Team.objects.all()
    aboutone = About.objects.all()
    data = {
        'teams' : teams,
        'aboutone' : aboutone,
    }

    return render(request,'webpages/about.html',data)
def services(request):
    return render(request,'webpages/services.html')
def contact(request):
    if request.method =='GET':
        return render(request,'webpages/contact.html')
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
    contactus = Contactus(full_name = full_name,phone_number = phone_number,email = email,company_name = company_name,subject = subject,message = message)
    contactus.save()
    messages.success(request,'Thanks for reaching out!')
    return redirect('contact')
