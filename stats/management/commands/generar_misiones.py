from django.core.management.base import BaseCommand
import datos_iniciales


class Command(BaseCommand):
    help = 'Genera misiones random para testing'

    def handle(self, *args, **options):
        datos_iniciales.generar_misiones()
        print("FINALIZADO GENERACIÓN DE MISIONES")
