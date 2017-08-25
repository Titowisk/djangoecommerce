# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category

class ProductList(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 3
    """
    Quando não é passado o nome de uma variável, essa classe(ListView) pega o nome do objeto a ser utilizado (Product),
    coloca no diminutivo e adiciona "_list" (product_list). Por isso que nesse caso não é necessário passar o context (mostrado abaixo).
    P.s: obiviamente há uma maneira de customizar o nome da variável a ser passada.
    context_object_name = nome_da_variavel_de_preferência.
    """

product_list = ProductList.as_view()
"""
def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, 'catalog/product_list.html', context)
No lugar dessa função foi utilizada a class based-view.
"""

class CategoryView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryView.as_view()

"""
def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category)
    }
    return render(request, 'catalog/category.html', context)
"""
# ----------------------------------------------------------------------------
"""
Do jeito que a função está, quando acesso a url .../produtos/design/, o django
vai executar a função dessa maneira: 
category(request, 'design')
O que no caso é ok, porém se a função tivesse mais parâmetros:
category(request, pk, slug)
A variável pk que iria receber o valor 'design' (o que ia bagunçar tudo).
Então é melhor pedir ao django que execute a função assim:
category(request, slug='design')
Isso é feito adicionando o ?P<parâmetro> na url. Assim o Django irá capturar
o valor, de forma NOMEADA. 
"""

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}

    return render(request, 'catalog/product.html', context)
