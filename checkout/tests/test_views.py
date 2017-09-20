# coding=utf-8

from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from model_mommy import mommy

from checkout.models import CartItem

class CreateCartItemTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make('catalog.Product')
        self.client = Client()
        self.url = reverse('checkout:create_cartitem', kwargs={'slug': self.product.slug})

    def tearDown(self):
        self.product.delete()
        CartItem.objects.all().delete()

    def test_add_cart_item_simple(self):
        response = self.client.get(self.url)
        redirect_url = reverse('checkout:cart_item')
        self.assertRedirects(response, redirect_url)
        self.assertEquals(CartItem.objects.count(), 1)

    def test_add_cart_item_complex(self):
        response = self.client.get(self.url)
        response = self.client.get(self.url)
        cart_item = CartItem.objects.get()
        self.assertEquals(cart_item.quantity, 2)


class CheckoutViewTestCase(TestCase):

    def setUp(self):
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()
        self.cart_item = mommy.make(CartItem)
        self.client = Client()

    def test_checkout_view(self):
        # Se o usuario tentar acessar o checkout sem logar, será redirecionado
        response = self.client.get(reverse('checkout:checkout'))
        redirect_url = '{}?next={}'.format(reverse(settings.LOGIN_URL), reverse('checkout:checkout'))
        self.assertRedirects(response, redirect_url)

        # Após logar, ele terá que ser novamente redirecionado para o checkout:checkout
        self.client.login(username=self.user.username, password='123')
        self.cart_item.cart_key = self.client.session.session_key   # Se não existir não funciona.
        self.cart_item.save()
        response = self.client.get(reverse('checkout:checkout'))
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_view_fail(self):
        # Caso o cart_key não for igual ao session_key
        self.client.login(username=self.user.username, password='123')
        self.cart_item.cart_key = 'blablabla'  # Se não existir não funciona.
        self.cart_item.save()
        response = self.client.get(reverse('checkout:checkout'))
        redirect_url = reverse('checkout:cart_item')
        self.assertRedirects(response, redirect_url)


