# Generated by Django 3.1.6 on 2021-02-25 13:07

import App.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_projet', models.CharField(max_length=30, verbose_name='Titre du projet')),
                ('duree_projet', models.IntegerField(default=0, verbose_name='Duree estimé ')),
                ('temps_alloue', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Temps alloué ')),
                ('besoins', models.TextField(max_length=250, verbose_name='Besoins ')),
                ('est_valide', models.BooleanField(default=False, verbose_name='Valide ')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name='Nom ')),
                ('prenom', models.CharField(max_length=30, verbose_name='Prenom ')),
                ('email', models.EmailField(max_length=254, validators=[App.models.is_esprit_mail], verbose_name='Email address ')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='App.user')),
            ],
            bases=('App.user',),
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='App.user')),
                ('group', models.CharField(max_length=30)),
            ],
            bases=('App.user',),
        ),
        migrations.CreateModel(
            name='MemberShipInProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_allocated_by_member', models.IntegerField(verbose_name='Temps alloué par le membre')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.projet')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='projet',
            name='createur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to='App.etudiant'),
        ),
        migrations.AddField(
            model_name='projet',
            name='membres',
            field=models.ManyToManyField(blank=True, through='App.MemberShipInProject', to='App.Etudiant'),
        ),
        migrations.AddField(
            model_name='projet',
            name='superviseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_coach', to='App.coach'),
        ),
    ]
