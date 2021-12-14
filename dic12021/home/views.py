from django.shortcuts import render

# Create your views here.

def index(request, **kwargs):
    return render(request, 'home/accueil.html')
    

def contact(request, **kwargs):
    return render(request, 'home/page_contact.html')

