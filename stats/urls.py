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
    path('myprofile/<int:pk>', views.MyProfileView.as_view(), name='my-profile'),

    # /stats/profile/<miembro_id>
    path('profile/<int:pk>', views.PublicProfileView.as_view(), name='profile'),

    # /stats/lista
    path('lista', views.AsistenciaListView.as_view(), name='stats-list'),

    # /stats/test/
    path('test-page', views.TestPage.as_view(), name='test-page'),

    # /stats/mision/crear/
    path('mision/crear/', views.CrearMision.as_view(), name='crear-mision'),

    # /stats/mision/crear/reporte/
    path('mision/crear/reporte', views.CrearMisionReporte.as_view(), name='crear-mision-reporte'),

    # /stats/mision/actualizar/<id_mision>
    path('mision/actualizar/<int:pk>', views.ActualizarMision.as_view(), name='actualizar-mision'),

    # /stats/calendario/
    path('calendario', views.CalendarView.as_view(), name='calendario'),

    # /stats/asistencia-mes/2019/6
    path('asistencia-mes/<int:year>/<int:month>', views.AsistenciaMes.as_view(), name='asistencia-mes'),

    # /stats/asistencia_mes_datatables/
    path('asistencia_mes_datatables/<int:year>/<int:month>', views.asistencia_datatables_ajax, name='asistencia_mes_datatables'),


    # /stats/misiongaleria-redirect/<int:mision_id>/<int:miembro_id>/<str:image>
    path('misiongaleria-redirect/<int:mision_id>/<int:miembro_id>', views.RedirectMisionGaleria.as_view(), name='misiongaleria-redirect'),
    path('misiongaleria-redirect/<int:mision_id>/<int:miembro_id>/<str:image>', views.RedirectMisionGaleria.as_view(), name='misiongaleria-redirect'),
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
    # urls for Unidad
    path('campana/', views.CampanaListView.as_view(), name='campana_list'),
    path('campana/create/', views.CampanaCreateView.as_view(), name='campana_create'),
    path('campana/detail/<int:pk>/', views.CampanaDetailView.as_view(), name='campana_detail'),
    path('campana/update/<int:pk>/', views.CampanaUpdateView.as_view(), name='campana_update'),
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
    path('mision/delete/<int:pk>/', views.MisionDeleteView.as_view(), name='mision_delete'),
)

urlpatterns += (
    # urls for Asistencia
    path('asistencia/', views.AsistenciaListView.as_view(), name='asistencia_list'),
    path('asistencia/create/', views.AsistenciaCreateView.as_view(), name='asistencia_create'),
    path('asistencia/detail/<int:pk>/', views.AsistenciaDetailView.as_view(), name='asistencia_detail'),
    path('asistencia/update/<int:pk>/', views.AsistenciaUpdateView.as_view(), name='asistencia_update'),
)

urlpatterns += (
    # urls for MisionGaleria
    path('misiongaleria/', views.MisionGaleriaListView.as_view(), name='misiongaleria_list'),
    path('misiongaleria/create/<int:mision_id>/', views.MisionGaleriaCreateView.as_view(), name='misiongaleria_create'),
    path('misiongaleria/detail/<int:pk>/', views.MisionGaleriaDetailView.as_view(), name='misiongaleria_detail'),
    path('misiongaleria/update/<int:pk>/', views.MisionGaleriaUpdateView.as_view(), name='misiongaleria_update'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

