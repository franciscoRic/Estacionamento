from django.contrib import admin
from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Parametros,
    MovRotativo,
    Menssalista,
    MovMenssalista,
)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'horas_total', 'total', 'pago')


class MovMenssalistaAdmin(admin.ModelAdmin):
    list_display = ('menssalista', 'data_pagamento', 'total')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Menssalista)
admin.site.register(MovMenssalista, MovMenssalistaAdmin)