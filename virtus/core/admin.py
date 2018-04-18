from django.contrib import admin
from virtus.core.models import Cliente, Endereco


class ClienteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['nome']}


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco)
