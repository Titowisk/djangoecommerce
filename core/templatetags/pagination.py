# coding=utf-8

from django.template import Library
"Registra a minha biblioteca de templates."

register = Library()

#Isto é um custom template tag criado pelo modo inclusion_tag().
@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
    context = {}
    context['paginator'] = paginator
    context['request'] = request
    context['page_obj'] = page_obj
    """
    Esse trecho é para permitir outros parâmetros no endereço web.
    Ver exemplo abaixo.
    """
    getvars = request.GET.copy()
    if 'page' in getvars:
        del getvars['page']
    if len(getvars) > 0:
        context['getvars'] = '&{0}'.format(getvars.urlencode())
    else:
        context['getvars'] = ''
    return context

"""
http://localhost:8000/catalogo/programacao/?search=dados
Quando eu clico no link da paginação essa url vira essa:
http://localhost:8000/catalogo/programacao/?page=2

ou seja, o trecho /?search=dados é perdido.
O que o prof fez permite que esse parâmetro continue acessivel.
http://localhost:8000/catalogo/programacao/?page=1&search=dados
"""


