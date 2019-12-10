from ..models import Clase, Rango, Nacionalidad, Rol, Unidad, Miembro, Mision, Asistencia, User, Campana


def asistencia_miembro(miembro, month, year):

    misiones_mes = Mision.objects.filter(oficial=True, fecha_finalizada__year=year, fecha_finalizada__month=month).order_by('fecha_finalizada','id')

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


def genera_calendario():
    misiones = Mision.objects.all()

    mision_list = []
    for mision in misiones:
        m = {}
        m['title'] = mision.print_tipo
        m['start'] = mision.fecha_finalizada
        m['end'] = mision.fecha_finalizada
        m['allDay'] = True
        m['url'] = mision.get_absolute_url()
        if mision.tipo == Mision.TIPO_CAMPANA or mision.tipo == Mision.TIPO_ENTRENAMIENTO or \
                mision.tipo == Mision.TIPO_GALA:
            m['className'] = "fc-event-danger"
        if mision.tipo == Mision.TIPO_IMPROVISADA:
            m['className'] = "fc-event-success"
        if mision.tipo == Mision.TIPO_CURSO:
            m['className'] = "fc-event-info"
        if mision.tipo == Mision.TIPO_OTRO or mision.tipo == Mision.TIPO_COOPERATIVA:
            m['className'] = "fc-event-warning"
        mision_list.append(m)
    return mision_list

