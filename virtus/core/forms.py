from django.forms import ModelForm
from virtus.core.models import Cliente


class ClienteModelForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'