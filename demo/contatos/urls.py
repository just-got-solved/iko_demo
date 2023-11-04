"ronaldo"
from django.urls import path
from . import views

urlpatterns = [
    path('incluir/', views.cadastrar_informacao_contato, name='add_contatos'),
]
