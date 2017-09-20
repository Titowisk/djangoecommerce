# coding=utf-8

from django.test import Client, TestCase
from django.conf import settings

from model_mommy import mommy

from checkout.models import CartItem, Order


class CartItemTestCase(TestCase):

    def setUp(self):
        mommy.make(CartItem, _quantity=3)   #Um carrinho de compras é criado com 3 produtos.

    def test_post_save_cart_item(self):
        cart_item = CartItem.objects.all()[0]   # Pega o primeiro produto.
        cart_item.quantity = 0  # atribui a quantidade 0
        cart_item.save()        # Salva, o sinal dispara e o produto em questão é removido do carrinho.
        self.assertEquals(CartItem.objects.count(), 2)  # Sobram apenas 2 produtos agora.

class OrderTestCase(TestCase):

    def setUp(self):
        self.cart_item = mommy.make(CartItem)
        self.user = mommy.make(settings.AUTH_USER_MODEL)

    def tearDown(self):
        self.cart_item.delete()
        self.user.delete()

    def test_create_order(self):
        Order.objects.create_order(self.user, [self.cart_item])  # def create_order(self, user, cart_items): lá do modelo.
        self.assertEquals(Order.objects.count(), 1)
        order = Order.objects.get()
        self.assertEquals(order.user, self.user)
        order_item = order.items.get()
        self.assertEquals(order_item.product, self.cart_item.product)
        self.assertEquals(order_item.quantity, self.cart_item.quantity)
        self.assertEquals(order_item.price, self.cart_item.price)

