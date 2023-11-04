from django.urls import path
from . import views

urlpatterns = [
    path('incluir/', views.cadastrar_informacao_contato, name='add_contatos'),
    path('cadastrar_contato/', views.cadastrar_informacao_contato, name='cadastrar_contato'),
]