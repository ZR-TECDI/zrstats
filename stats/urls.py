from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static\

app_name = 'stats'

urlpatterns = [
    # /stats/
    path('', views.index_view, name='index'),

    # /stats/to-profile/
    path('to-profile', views.RedirectToProfile.as_view(), name='redirect_to_profile'),

    # /stats/profile/<user_id>
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),

    # /stats/upload
    path('upload', views.upload_file, name='upload'),

    # /stats/lista
    path('lista', views.AsistenciaListView.as_view(), name='stats-list'),
]

urlpatterns += (
    # urls for Clase
    path('clase/', views.ClaseListView.as_view(), name='clase_list'),
    path('clase/create/', views.ClaseCreateView.as_view(), name='clase_create'),
    path('clase/detail/<int:pk>/', views.ClaseDetailView.as_view(), name='clase_detail'),
    path('clase/update/<int:pk>/', views.ClaseUpdateView.as_view(), name='clase_update'),
)

urlpatterns += (
    # urls for Rango
    path('rango/', views.RangoListView.as_view(), name='rango_list'),
    path('rango/create/', views.RangoCreateView.as_view(), name='rango_create'),
    path('rango/detail/<int:pk>/', views.RangoDetailView.as_view(), name='rango_detail'),
    path('rango/update/<int:pk>/', views.RangoUpdateView.as_view(), name='rango_update'),
)

urlpatterns += (
    # urls for Nacionalidad
    path('nacionalidad/', views.NacionalidadListView.as_view(), name='nacionalidad_list'),
    path('nacionalidad/create/', views.NacionalidadCreateView.as_view(), name='nacionalidad_create'),
    path('nacionalidad/detail/<int:pk>/', views.NacionalidadDetailView.as_view(), name='nacionalidad_detail'),
    path('nacionalidad/update/<int:pk>/', views.NacionalidadUpdateView.as_view(), name='nacionalidad_update'),
)

urlpatterns += (
    # urls for Rol
    path('rol/', views.RolListView.as_view(), name='rol_list'),
    path('rol/create/', views.RolCreateView.as_view(), name='rol_create'),
    path('rol/detail/<int:pk>/', views.RolDetailView.as_view(), name='rol_detail'),
    path('rol/update/<int:pk>/', views.RolUpdateView.as_view(), name='rol_update'),
)

urlpatterns += (
    # urls for Unidad
    path('unidad/', views.UnidadListView.as_view(), name='unidad_list'),
    path('unidad/create/', views.UnidadCreateView.as_view(), name='unidad_create'),
    path('unidad/detail/<int:pk>/', views.UnidadDetailView.as_view(), name='unidad_detail'),
    path('unidad/update/<int:pk>/', views.UnidadUpdateView.as_view(), name='unidad_update'),
)

urlpatterns += (
    # urls for Miembro
    path('miembro/', views.MiembroListView.as_view(), name='miembro_list'),
    path('miembro/create/', views.MiembroCreateView.as_view(), name='miembro_create'),
    path('miembro/detail/<int:pk>/', views.MiembroDetailView.as_view(), name='miembro_detail'),
    path('miembro/update/<int:pk>/', views.MiembroUpdateView.as_view(), name='miembro_update'),
)

urlpatterns += (
    # urls for Mision
    path('mision/', views.MisionListView.as_view(), name='mision_list'),
    path('mision/create/', views.MisionCreateView.as_view(), name='mision_create'),
    path('mision/detail/<int:pk>/', views.MisionDetailView.as_view(), name='mision_detail'),
    path('mision/update/<int:pk>/', views.MisionUpdateView.as_view(), name='mision_update'),
)

urlpatterns += (
    # urls for Asistencia
    path('asistencia/', views.AsistenciaListView.as_view(), name='asistencia_list'),
    path('asistencia/create/', views.AsistenciaCreateView.as_view(), name='asistencia_create'),
    path('asistencia/detail/<int:pk>/', views.AsistenciaDetailView.as_view(), name='asistencia_detail'),
    path('asistencia/update/<int:pk>/', views.AsistenciaUpdateView.as_view(), name='asistencia_update'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

