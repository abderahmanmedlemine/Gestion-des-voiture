from enum import member
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from bookstore.models import membre

# def home(request):
#     return HttpResponse('Home page ')
#render 5assa bi templates 2dgiss bik templates

def home(request):
    return render(request,'home.html')

def constomer(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')

        if nom and prenom:  # Vérification pour éviter les valeurs None
            data = membre(nom=nom, prenom=prenom)  # Utilisation du modèle correct
            data.save()
    return render(request, 'constomer.html', {'m': membre.objects.all()})

def product(request):
    return render(request,'product.html')

def base(request):
    return render(request,'base.html')


