# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^carrinha/adicionar/(?P<slug>[\w_-]+)/$',
        views.create_cartitem,
        name='create_cartitem'),
    url(r'^carrinho/$', views.cart_item, name='cart_item'),
    url(r'^finalizar-compras/$', views.checkout, name='checkout'),
]
