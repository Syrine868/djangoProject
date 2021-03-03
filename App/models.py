from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Sum, Count


def is_esprit_mail(value):
    if not str(value).endswith('@esprit.tn'):
        raise ValidationError("Votre E-mail est incorrect", params={'value': value})


# Create your models here.
class User(models.Model):
    nom = models.CharField('Nom ', max_length=30)
    prenom = models.CharField('Prenom ', max_length=30)
    email = models.EmailField('Email address ', validators=[is_esprit_mail])

    def __str__(self):
        return f'{self.nom}  {self.prenom}'


class Etudiant(User):
    group = models.CharField(max_length=30)




class Coach(User):
    def __str__(self):
        return f'{self.nom} {self.email}'

    def nb_projects_by_coach(self):
        nb_projets = Projet.objects.filter(superviseur=self.pk)
        nb = nb_projets.all().aggregate(Count('nom_projet'))
        return nb['nom_projet__count'] or 0


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
    createur = models.OneToOneField(
        Etudiant,
        on_delete=models.CASCADE,
        related_name='project_owner'
    )
    membres = models.ManyToManyField(
        Etudiant,
        through='MemberShipInProject',
        blank=True
    )

    def temps_total_membre(self):
        list_member = MemberShipInProject.objects.filter(projet=self.pk)
        sum_allocated = list_member.all().aggregate(Sum('time_allocated_by_member'))
        return sum_allocated['time_allocated_by_member__sum'] or 0


class MemberShipInProject(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    time_allocated_by_member = models.IntegerField('Temps alloué par le membre')


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    website = models.URLField()
