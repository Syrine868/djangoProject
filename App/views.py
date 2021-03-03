from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Bonjour page index')


def projet_id(request, id):
    return HttpResponse("Id_projet : %s" % id)


def projet(request):
    return render(request, 'App/index.html')
