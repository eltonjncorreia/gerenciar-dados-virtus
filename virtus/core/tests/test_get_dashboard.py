from django.test import TestCase
from django.urls import reverse


class DashboardTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('core:dashboard'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/index.html')
