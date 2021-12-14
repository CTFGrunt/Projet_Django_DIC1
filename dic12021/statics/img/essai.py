from django.db import models

class Departement (models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=80, default ="")
    description = models.TextField()

class Meta :
    verbosename = "département"
    verbosename_plural = "départements"