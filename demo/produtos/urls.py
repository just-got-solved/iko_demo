from django.urls import path
from . import views

urlpatterns = [
    path('incluir/', views.add_produto, name='add_produtos'),
    path('lista/', views.lista_produtos, name='lista_produtos'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
]