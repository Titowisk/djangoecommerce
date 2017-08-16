# coding=utf-8

from django.test import TestCase, Client

from model_mommy import mommy

from django.core.urlresolvers import reverse

from catalog.models import Category, Product

class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = mommy.make('catalog.Product', _quantity=10)

    def tearDown(self):
        Product.objects.all().delete()

    """
    Testa se o cliente consegue acessar o html e se o html acessado é o desejado.
    """
    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    """
    Testa se o contexto contém os 10 produtos criados no setUp.
    """
    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('product_list' in response.context)
        product_list = response.context['product_list']
        self.assertEquals(product_list.count(), 10)


class CategoryTestCase(TestCase):
    pass

class ProductTestCase(TestCase):
    pass