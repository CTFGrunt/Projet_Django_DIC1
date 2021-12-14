from django.contrib import admin
from departement.models import Departement,User,Etudiant,Professeur,Classe,UE_matiere,Matière
# Register your models here.
admin.site.register(Departement)
#admin.site.register(User)
#admin.site.register(Etudiant)
#admin.site.register(Professeur)
admin.site.register(Classe)
admin.site.register(Matière)
admin.site.register(UE_matiere)



class ProfesseurAdmin(admin.ModelAdmin):
    list_display=('nom','mail','display_matière','date_d_adhesion')

admin.site.register(Professeur,ProfesseurAdmin)

class EtudiantAdmin(admin.ModelAdmin):
    list_display=('prenom','nom','mail')

admin.site.register(Etudiant,EtudiantAdmin)




