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
        self.assertEquals(product_list.count(), 3)
        """
        O teste cria 10 produtos, então o paginator deve criar
        4 páginas (3 pagas de 3 produtos + 1 pag. com 1 produto).
        """
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 4)

    def test_page_not_found(self):
        """
        Quando a página requisitar um endereço que não existe, o django tem que retornar um error 404.
        """
        response = self.client.get('{}?page=5'.format(self.url))
        self.assertEquals(response.status_code, 404)


class CategoryTestCase(TestCase):
    pass

class ProductTestCase(TestCase):
    pass