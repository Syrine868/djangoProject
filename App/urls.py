from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('index/', views.index, name='index'),
    path('projet/<int:id>/', views.projet_id),
    path('/', views.projet),
    path('liste/', views.liste_projet),
    path('detail/<int:id>/', views.detail, name="D"),
    path('ListView/', projet_liste.as_view()),
    path('DetailView/<int:pk>/', projet_detail.as_view(), name="detail")
]
