from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Classe(models.Model):
    dept=models.TextChoices('dept','GEM GC TC AERO GIT')
    nom_classe=models.CharField(max_length=100)
    description_classe=models.TextField(max_length=1000)
    departement=models.CharField(max_length=100,blank=True,choices=dept.choices)

    def __str__(self) -> str:
        return self.nom_classe


class UE_matiere(models.Model):
    nom_UE=models.CharField('le nom de l\'unité de l\'enseignement',max_length=100)
    code_UE=models.CharField(max_length=100,primary_key=True)
    classe=models.ForeignKey(Classe,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom_UE

    def coef_UE(self):
        pass
    def credit_UE(self):
        pass


class Matière(models.Model):
    nom_matiere=models.CharField('le nom de la matière',max_length=100)
    code_matiere=models.CharField(max_length=100,primary_key=True)
    coef_matiere=models.IntegerField()
    credit_matiere=models.IntegerField()
    quota_horaire=models.IntegerField()
    description_matiere=models.TextField()
    nom_UE=models.ForeignKey(UE_matiere,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_matiere



class User(models.Model):
    prenom=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)
    mail=models.EmailField()

    def __str__(self):
        return self.prenom
    
class Etudiant(User):
    password=models.CharField(max_length=100)
    date_de_naissance=models.DateField()
    lieu_de_naissance=models.CharField (max_length=100,)  

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.mail}"


class Professeur(User):
    chef=[(1,'True'),(2,'False')]
    contact_prof=models.CharField("Contact du prof",max_length=100)
    date_d_adhesion=models.DateField()
    chef_departement=models.CharField(max_length=100,blank=True,choices=chef)
    matieres=models.ManyToManyField(Matière)


    def __str__(self):
        return self.prenom

    def display_matière(self):
        return ','.join(matière.nom_matiere for matière in self.matieres.all())

    display_matière.short_description='Matière'

class Departement(models.Model):
    nom_departement=models.TextChoices('dept','GEM GC TC AERO GIT')
    nom=models.CharField(max_length=100,blank=True,choices=nom_departement.choices)
    mail_departement=models.EmailField()
    numero_departement=models.CharField(max_length=12)
    description_dept=models.TextField(max_length=1000)
    professeurs=models.ManyToManyField(Professeur)



    def __str__(self) -> str:
        return self.nom











