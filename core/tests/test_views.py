# coding=utf-8
from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        """
        Evitar repetição de código.
        """
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_status_code(self):
        """
        Serve para verificar se o site está acessivel. (retorna código 200).
        O '/' é o path para o site.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
        Verifica se o template desejado está realmente sendo utilizado.
        """
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

    