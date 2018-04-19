from django.forms import ModelForm
from virtus.core.models import Cliente, Endereco


class ClienteModelForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class EnderecoModelForm(ModelForm):

    class Meta:
        model = Endereco
        fields = '__all__'
