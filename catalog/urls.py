# coding=utf-8

from django.conf.urls import url


from catalog import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
] 

"""
catalogo/slug da categoria/produto
Isso não é bom caso futuramente um produto pertença a mais de uma categoria.

"""
