# coding=utf-8

from django.test import TestCase

from model_mommy import mommy

from django.core.urlresolvers import reverse

from catalog.models import Category, Product

"""
Para testar apenas essa app, é só digitar:
$python manage.py test nome_da_aplicação
No caso ficaria:
$python manage.py test catalog
"""

class CategoryTestCase(TestCase):

    """
    Em vez de chamar manualmente os models criados e parametrizar um por um,
    o model_mommy faz isso 'atuomagically'.
    """
    def setUp(self):
        self.category = mommy.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:category', kwargs={'slug': self.category.slug})
        )

class ProductTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make(Product, slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.product.get_absolute_url(),
            reverse('catalog:product', kwargs={'slug': 'produto'})
        )
