from django.urls import include, path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_mov_rotativo,
    lista_menssalista,
    lista_mov_menssalista,
    pessoa_novo,
    veiculo_novo,
    mov_rotativo_novo,
    menssalista_novo,
    mov_menssalista_novo,
    pessoa_update,
    veiculo_update,
    mov_rotativo_update,
    menssalista_update,
    mov_menssalista_update,
    pessoa_delete,
    veiculo_delete
)
    

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa_update/<int:id>', pessoa_update, name='core_pessoa_update'),
    path('pessoa_delete/<int:id>', pessoa_delete, name='core_pessoa_delete'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos_novo/', veiculo_novo, name='core_veiculo_novo'),  
    path('veiculo_update/<int:id>', veiculo_update, name='core_veiculo_update'),  
    path('veiculo_delete/<int:id>', veiculo_delete, name='core_veiculo_delete'),
    
    path('mov_rot/', lista_mov_rotativo, name='core_mov_rot_lista'),
    path('mov_rot_novo/', mov_rotativo_novo, name='core_mov_rot_novo'),
    path('mov_rot_update/<int:id>', mov_rotativo_update, name='core_mov_rot_update'),  
    
    path('menssalistas/', lista_menssalista, name='core_lista_menssalista'),
    path('menssalistas_novo/', menssalista_novo, name='core_menssalista_novo'),
    path('menssalista_update/<int:id>', menssalista_update, name='core_menssalista_update'),
    
    path('mov_mensal/', lista_mov_menssalista, name='core_lista_mov_menssalista'),
    path('mov_mensal_novo/', mov_menssalista_novo, name='core_mov_menssalista_novo'),
    path('mov_mensal_update/<int:id>', mov_menssalista_update, name='core_mov_menssalista_update'),

]
