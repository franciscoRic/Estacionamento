from django.urls import include, path
from .views import home, lista_pessoas, lista_veiculos, lista_movrotativo


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov_rot_lista/', lista_movrotativo, name='core_mov_rot_lista'),

]
