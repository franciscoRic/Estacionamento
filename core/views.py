from django.shortcuts import render


def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context)

