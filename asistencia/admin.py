from django.contrib import admin
from .models import Miembro, Clase, Asistencia, Nacionalidad, Rango, Unidad, Rol

admin.site.register(Miembro)
admin.site.register(Clase)
admin.site.register(Asistencia)
admin.site.register(Nacionalidad)
admin.site.register(Rango)
admin.site.register(Unidad)
admin.site.register(Rol)

