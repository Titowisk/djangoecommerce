# coding=utf-8
from django.shortcuts import render

from .models import Product, Category

def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, 'catalog/product_list.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category)
    }
    return render(request, 'catalog/category.html', context)
"""
Do jeito que a função está, quando acesso a url .../produtos/design/, o django
vai executar a função dessa maneira: 
category(request, 'design')
O que no caso é ok, porém se a função tivesse mais parâmetros:
category(request, pk, slug)
A variável pk que iria receber o valor 'design' (o que ia bagunçar tudo).
Então é melhor pedir ao django que execute a função assim:
category(request, slug='desing')
Isso é feito adicionando o ?P<parâmetro> na url. Assim o Django irá capturar
o valor, de forma NOMEADA. 
"""

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}

    return render(request, 'catalog/product.html', context)
