from django.test import TestCase
from django.shortcuts import resolve_url as r

from virtus.core.forms import ClienteModelForm
from virtus.core.models import Cliente


class EditarTest(TestCase):
    def setUp(self):
        self.obj = Cliente.objects.create(nome='Joao soares',
                                          email='joao@joao.com',
                                          telefone='88988991199',
                                          cpf='02304567809',
                                          slug='joao-soares')

        self.resp = self.client.get(r('core:edit-cliente', self.obj.slug))

    def test_get(self):
        """retorno de status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """obtem template"""
        self.assertTemplateUsed(self.resp, 'core/edicao.html')

    def test_str(self):
        """tem metodo str"""
        self.assertEqual('Joao soares', str(self.obj))

    def test_context(self):
        """tem instancia de form no contexto"""
        form = self.resp.context['form']
        self.assertIsInstance(form, ClienteModelForm)

    def test_html(self):
        """Html contem tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 4),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """html contem csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_create(self):
        """testa se existe o queryset"""
        self.assertTrue(Cliente.objects.exists())

    def test_contens(self):
        contents = (self.obj.nome, self.obj.cpf,
                    self.obj.email, self.obj.telefone)

        with self.subTest():
            for expect in contents:
                self.assertContains(self.resp, expect)





