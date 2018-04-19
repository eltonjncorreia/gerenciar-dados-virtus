from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from virtus.core.forms import ClienteModelForm, EnderecoModelForm
from virtus.core.models import Cliente, Endereco


def dashboard(request):
    clientes = Cliente.objects.prefetch_related('enderecos').all()
    return render(request, 'core/index.html', {'clientes': clientes})


def edit(request, slug):
    cliente = Cliente.objects.get(slug=slug)
    endereco = Endereco.objects.get(cliente=cliente)

    if request.method == 'POST':
        form_endereco = EnderecoModelForm(request.POST, instance=endereco)
        form_cliente = ClienteModelForm(request.POST, instance=cliente)

        if form_endereco.is_valid() and form_cliente.is_valid():
            form_endereco.save()
            form_cliente.save()

            messages.success(request, 'Atualização realizada')
            return HttpResponseRedirect(r('core:edit-cliente', slug=slug))
    else:
        form_endereco = EnderecoModelForm(instance=endereco)
        form_cliente = ClienteModelForm(instance=cliente)

    return render(request, 'core/edicao.html', {'endereco': form_endereco, 'cliente': form_cliente, 'clientes': cliente.slug})


def deletar(request, slug):
    Cliente.objects.filter(slug=slug).delete()
    messages.success(request, 'Deletado com sucesso')
    return HttpResponseRedirect(r('core:dashboard'))

