from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *

# Create your views here.
from App.models import Projet


def index(request):
    return HttpResponse('Bonjour page index')


def projet_id(request, id):
    return HttpResponse("Id_projet : %s" % id)


def projet(request):
    return render(request, 'App/index.html')


# @login_required(login_url='login')
def liste_projet(request):
    projets = Projet.objects.all()
    context = {'p': projets}
    return render(request, 'App/list.html', context)


def detail(request, id):
    projet = Projet.objects.get(pk=id)
    return render(request, 'App/detail.html', {'pp': projet})


class projet_liste(ListView):
    model = Projet
    # App/projet_list.html par defaut
    template_name = "ListeView.html"
    context_object_name = 'p'
    # pour inverser l'ordre m asc l desc nzid -
    ordering = ['-temps_alloue']


class projet_detail(DetailView):
    model = Projet
    context_object_name = 'pp'


def logout_user(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = authenticate()
            # login(user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'f': form})


def accueil(request):
    return render(request, 'accueil.html')
