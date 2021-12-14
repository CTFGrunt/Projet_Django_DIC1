from django.shortcuts import render
from departement.models import Etudiant,Professeur,Departement, Matière, UE_matiere, User, Classe

# Create your views here.
def index(request, **kwargs):
    return render(request, 'home/accueil.html')