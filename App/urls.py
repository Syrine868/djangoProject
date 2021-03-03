from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('projet/<int:id>/', views.projet_id),
    path('/', views.projet)
]
