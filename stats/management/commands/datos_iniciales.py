from django.core.management.base import BaseCommand
import datos_iniciales
from stats.models import User


class Command(BaseCommand):
    help = 'Carga datos iniciales'

    def handle(self, *args, **options):
        datos_iniciales.borra_todo()
        datos_iniciales.crear_unidades()
        datos_iniciales.crear_rango()
        datos_iniciales.crear_rol()
        datos_iniciales.crear_clase()
        datos_iniciales.crear_naciones()
        #datos_iniciales.agregar_miembros() # Deprecado, ahora los sacamos del excel de asistencia
        datos_iniciales.procesa_xsl()
        # Le pongo permisos al usuario admin
        user = User.objects.create()
        user.username = "Admin"
        user.password = "admin"
        user.miembro.nombre = "Admin"
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("FINALIZADO DATOS INICIALES")

