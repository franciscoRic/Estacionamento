from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, Menssalista, MovMenssalista, Veiculo

from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MenssalistaForm, MovMenssalistaForm

def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = { 'pessoas': pessoas, 'form': form }
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoas.html', data)

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculos.html', data)

def lista_mov_rotativo(request):
    movrotativo = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movrotativos': movrotativo, 'form': form}
    return render(request, 'core/lista_mov_rot.html', data)

def mov_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mov_rot_lista')

def mov_rotativo_update(request, id):
    data = {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('core_mov_rot_lista')
    else:
        return render(request, 'core/update_mov_rot.html', data)

def lista_menssalista(request):
    menssalista = Menssalista.objects.all()
    form = MenssalistaForm()
    data = {'menssalistas': menssalista, 'form': form}
    return render(request, 'core/lista_menssalista.html', data)

def menssalista_novo(request):
    form = MenssalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_menssalista')

def lista_mov_menssalista(request):
    mov_menssalistas = MovMenssalista.objects.all()
    form = MovMenssalistaForm()
    data = {'mov_menssalistas': mov_menssalistas, 'form': form}
    return render(request, 'core/lista_mov_menssalista.html', data)

def mov_menssalista_novo(request):
    form = MovMenssalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_menssalista')
