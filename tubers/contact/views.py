from django.shortcuts import render
from contact.models import Detail
# Create your views here.
def detail(request):
    mails = Detail.objects.all()
    data = {
        'mails' : mails,
        }
    return render(request,'includes/header.html',data)

