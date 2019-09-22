from ..models import Clase, Rango, Nacionalidad, Rol, Unidad, Miembro, Mision, Asistencia, User, Campana


def asistencia_miembro(miembro, month, year):

    misiones_mes = Mision.objects.filter(oficial=True, fecha_finalizada__year=year, fecha_finalizada__month=month)

    asistencia = []
    for mision in misiones_mes:
        try:
            a = Asistencia.objects.get(fecha__month=month, fecha__year=year, miembro=miembro, mision=mision)
        except Asistencia.DoesNotExist:
            a = None
        asistencia.append(a)

    result = {}
    result['miembro'] = miembro
    result['asistencia'] = asistencia
    return result

