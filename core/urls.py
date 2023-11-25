from .views import registerdoacao, home, doacoes, excluir_prod, filter_prod, creditos
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registerdoacao', registerdoacao, name='registerdoacao'),
    path('', home, name='home'),
    path('doacoes', doacoes, name='doacoes'),
    path('produto/<int:produto_id>/excluir/', excluir_prod, name='excluir_prod'),
    path('filter_prod', filter_prod, name='filter_prod'),
    path('creditos', creditos, name='creditos')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)