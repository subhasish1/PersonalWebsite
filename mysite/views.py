from django.shortcuts import render
from django.conf.urls.static import static
from .models import Contact

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'mysite/index.html')
def portfolio(request):
    return render(request,'mysite/portfolio.html')
def contact(request):
    if request.method=='POST':
        eamil_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email = eamil_r,subject = subject_r, message=message_r)
        c.save()
        return render(request,'mysite/contact.html')
    else:
        return render(request,'mysite/contact.html')
