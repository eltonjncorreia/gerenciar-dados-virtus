from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from virtus.core.forms import ClienteModelForm
from virtus.core.models import Cliente, Endereco


def dashboard(request):
    clientes = Cliente.objects.prefetch_related('enderecos').all()
    return render(request, 'core/index.html', {'clientes': clientes})


def edit(request, slug):
    cliente = Cliente.objects.get(slug=slug)

    if request.method == 'POST':
        form = ClienteModelForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(r('core:dashboard'))
    else:
        form = ClienteModelForm(instance=cliente)

    return render(request, 'core/edicao.html', {'form': form})

