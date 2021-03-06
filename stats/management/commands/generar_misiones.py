from django.core.management.base import BaseCommand
import datos_iniciales
from stats.models import User


class Command(BaseCommand):
    help = 'Genera misiones random para testing'

    def handle(self, *args, **options):
        datos_iniciales.crear_unidades()
        datos_iniciales.crear_rango()
        datos_iniciales.crear_rol()
        datos_iniciales.crear_clase()
        datos_iniciales.crear_naciones()
        datos_iniciales.agregar_miembros()
        datos_iniciales.generar_misiones()
        # Le pongo permisos al usuario admin
        user = User.objects.get(username="Admin")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("FINALIZADO DATOS INICIALES")
