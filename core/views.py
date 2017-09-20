# coding=utf-8

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.contrib import messages

from .forms import ContactForm

User = get_user_model()

"""
def index(request):
    return render(request, 'index.html')

No lugar dessa função será utilizada uma classe. Utilizando classes, o código utilizado torna-se mais reaproveitável, facilitando a implementação de apps de um projeto em outro.
"""
class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()


"""
Como funciona a função send_mail. Pág 433 do Django Documentation.
send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
"""

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido.')

    context = {'form': form, 'success': success}
    return render(request, 'contact.html', context)

def product(request):
    return render(request, 'product.html')


