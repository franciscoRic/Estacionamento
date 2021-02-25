from django.shortcuts import render
from .models import Pessoa, Veiculo, MovRotativo, Menssalista, MovMenssalista


def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', { 'pessoas': pessoas })

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})

def lista_mov_rotativo(request):
    movrotativo = MovRotativo.objects.all()
    return render(request, 'core/lista_mov_rot.html', {'movrotativos': movrotativo})

def lista_menssalista(request):
    menssalista = Menssalista.objects.all()
    return render(request, 'core/lista_menssalista.html', {'menssalistas': menssalista})

def lista_mov_menssalista(request):
    mov_menssalistas = MovMenssalista.objects.all()
    return render(request, 'core/lista_mov_menssalista.html', {'mov_menssalistas': mov_menssalistas})
