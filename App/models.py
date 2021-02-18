from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class User(models.Model):
    nom = models.CharField('Nom ', max_length=30)
    prenom = models.CharField('Prenom ', max_length=30)
    email = models.EmailField('Email address :')


class Etudiant(User):
    pass


class Coach(User):
    pass


class Projet(models.Model):
    nom_projet = models.CharField('Titre du projet', max_length=30)
    duree_projet = models.IntegerField('Duree estimé ', default=0)
    temps_alloue = models.IntegerField('Temps alloué ', validators=[MinValueValidator(1), MaxValueValidator(10)])
    besoins = models.TextField('Besoins ', max_length=250)
    est_valide = models.BooleanField('Valide ', default=False)
    superviseur = models.ForeignKey(Coach,
                                    related_name='project_coach',
                                    on_delete=models.SET_NULL,
                                    # on_delete=models.CASCADE()
                                    # blank=True,
                                    null=True
                                    )
