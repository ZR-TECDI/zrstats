from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static\

app_name = 'asistencia'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('upload', views.upload_file, name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)