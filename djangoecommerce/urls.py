from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

from core import views
from catalog import views as views_catalog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
]

# Apens em produção será servido arquivos media dessa forma
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
