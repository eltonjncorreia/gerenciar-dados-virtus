from django.test import TestCase
from virtus.core.forms import ClienteModelForm


class ClienteFormEditTest(TestCase):

    def test_form_tem_field(self):
        """Form tem fields"""
        form = ClienteModelForm()
        expect = ['nome', 'email', 'telefone', 'cpf', 'slug']
        self.assertSequenceEqual(expect, list(form.fields))

    def test_cpf_is_digito(self):
        form = self.validar_form(cpf='ABDC23455')
        self.assertFormErrorMessage(form, 'cpf', 'Informe um valor válido.')

    def test_email_nao_optional(self):
        form = self.validar_form(email='')
        self.assertTrue(form.errors)

    def test_telefone_nao_optional(self):
        form = self.validar_form(telefone='')
        self.assertTrue(form.errors)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def validar_form(self, **kwargs):
        """recebe um dicionario e verifica se é valido os campos"""
        valid = dict(nome="Elton Jefferson", cpf='12345678901',
                     telefone="21212121", email='elton@correia.net')

        data = dict(valid, **kwargs)
        form = ClienteModelForm(data)
        form.is_valid()
        return form

