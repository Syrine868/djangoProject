from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('index/', views.index, name='index'),
    path('projet/<int:id>/', views.projet_id),
    path('/', views.projet),
    path('liste/', views.liste_projet, name='liste'),
    path('detail/<int:id>/', views.detail, name="D"),
    path('ListView/', projet_liste.as_view()),
    path('DetailView/<int:pk>/', projet_detail.as_view(), name="detail"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accueil/', views.accueil, name='accueil')
]
