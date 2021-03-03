from django.contrib import admin
from .models import *


# Register your models here.
class Members(admin.TabularInline):
    model = MemberShipInProject


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    inlines = (Members,)
    list_display = ('nom_projet', 'duree_projet', 'createur', 'superviseur', 'est_valide', 'temps_total_membre')
    fieldsets = (
        ('A propos', {'fields': ('nom_projet',
                                 'besoins',
                                 )}),
        ('Etat', {'fields': ('est_valide',)}),
        ('Duree', {'fields': ('duree_projet',
                              'temps_alloue'
                              )}),
        ('Les coachs', {'fields': ('createur',
                                   'superviseur'
                                   )})

    )


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('nom',
                    'prenom',
                    'email',
                    'nb_projects_by_coach')
    fieldsets = (
        ('Informations Personnels ',
         {'fields': ('nom', 'prenom')}),
        ('Contact Email', {'fields': ('email',)})
    )


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom',
                    'prenom',
                    'email',
                    'group',

                    )
    list_select_related = ('project_owner', 'user_ptr')
    fieldsets = (
        ('Informations Personnels ',
         {'fields': ('nom', 'prenom')}),
        ('Contact Email', {'fields': ('email',)}),
        ('Groupes', {'fields': ('group',)})
    )


# admin.site.register(Coach)
# admin.site.register(Etudiant)
# admin.site.register(Projet, ProjetAdmin)
# admin.site.register(Projet, ProjetAdmin)
