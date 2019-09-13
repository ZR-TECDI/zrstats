"""
WSGI config for zrstats project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zrstats.settings')

application = get_wsgi_application()

# Cambiar primera_vez a True para cargar los datos iniciales en la Base de Datos
# 1) primera_vez = True.
# 2) Ejecutar Django, dejar que carguen Unidades, Rangos, Clases, Paises, etc..
# 3) Detener Django y volver a poner primera_vez = False
# 4) profit
primera_vez = False

if primera_vez:
    import datos_iniciales
    datos_iniciales.main()

