from django.urls import include, path
from .views import (
    home, lista_pessoas, lista_veiculos, lista_mov_rotativo, lista_menssalista, lista_mov_menssalista
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov_rot/', lista_mov_rotativo, name='core_mov_rot_lista'),
    path('menssalistas/', lista_menssalista, name='core_lista_menssalista'),
    path('mov_mensal/', lista_mov_menssalista, name='core_lista_mov_menssalista'),

]
