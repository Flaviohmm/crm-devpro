from django.contrib import admin

# Register your models here.
from clientes.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'contactado_em', 'foi_contactado']
    fields = ['nome', 'foi_contactado']
