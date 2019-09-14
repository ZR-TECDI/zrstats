from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static\

app_name = 'stats'

urlpatterns = [
    # /stats/
    path('', views.index_view, name='index'),
    # /stats/upload
    path('upload', views.upload_file, name='upload'),
    # /stats/lista
    path('lista', views.AsistenciaListView.as_view(), name='stats-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

