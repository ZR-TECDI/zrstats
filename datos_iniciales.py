"""Agrega los datos iniciales de forma automática"""

from asistencia.models import *


def crear_unidades():
    unidades_dict = {
        'altm': ['Alto Mando', 'ALTM'],
        'infm': ['Inf. de Marines', 'IMZR'],
        'paraca': ['Paracaidistas', 'PARACA'],
        'echo': ['Espectro', 'ECHO'],
        'cab': ['Caballería', 'CAB'],
        'fazr': ['Fuerza Aérea', 'FAZR'],
    }

    print('Creando Unidades...')

    for var, array in unidades_dict.items():
        var = Unidad.objects.create()
        var.nombre = array[0]
        var.abreviatura = array[1]
        var.save()


def crear_rango():
    rangos_dict = {
        'may': ['Mayor', 'May', 0],
        'cap': ['Capitán', 'Cap', 1],
        'tte': ['Teniente', 'Tte', 2],
        'alf': ['Alférez', 'Alf', 3],
        'sgtm': ['Sargento Mayor', 'SgtM', 4],
        'sgt1': ['Sargento 1º', 'Sgt1', 5],
        'sgt': ['Sargento', 'Sgt', 6],
        'cbo1': ['Cabo 1º', 'Cbo1', 7],
        'cbo': ["Cabo", 'Cbo', 8],
        'dis': ['Distinguido', 'Dis', 9],
        'inf': ['Infante', 'Inf', 10],
        'rct': ['Recluta', 'Rct', 11],
        'asp': ['Aspirante', 'Asp', 12]
    }

    print('Creando rangos...')

    for var, array in rangos_dict.items():
        var = Rango.objects.create()
        var.rango = array[0]
        var.abreviatura = array[1]
        var.orden = array[2]
        var.save()


def crear_rol():
    roles_dict = {
        'nada': ['--', '--'],
        'cmd': ['Comandante Unidad', 'CMD'],
        'ce': ['Comandante Escuadra', 'CE'],
        'lea': ['Líder Equipo A', 'LEA'],
        'leb': ['Líder Equipo B', 'LEB']
    }

    print('Creando roles...')

    for var, array in roles_dict.items():
        var = Rol.objects.create()
        var.rol = array[0]
        var.abreviatura = array[1]
        var.save()


def crear_clase():
    clases_dict = {
        'nada': ['--', '--'],
        'fl': ['Fusilero', 'FL'],
        'mg': ['Ametrallador', 'MG'],
        'at': ['Antitanque', 'AT'],
        'gl': ['Granadero', 'GL'],
        'mc': ['Médico de combate', 'MC'],
        'od': ['Operador de dron', 'OD'],
        'ro': ['Radio operador', 'RO'],
        'te': ['Tirador de escuadra', 'TE']
    }

    print('Creando clases...')

    for var, array in clases_dict.items():
        var = Clase.objects.create()
        var.clase = array[0]
        var.abreviatura = array[1]
        var.save()


def crear_naciones():
    # TODO no habrá un template con todos los países como en cualquier formulario web?
    naciones_dict = {
        'arg': ['Argentina', 'ARG'],
        'cl': ['Chile', 'CL'],
        'col': ['Colombia', 'COL'],
        'cr': ['Costa Rica', 'CR'],
        'sv': ['El Salvador', 'SV'],
        'jp': ['Japón', 'JP'],
        'mx': ['México', 'MX'],
        'pa': ['Panamá', 'PA'],
        'py': ['Paraguay', 'PY'],
        'pe': ['Perú', 'PE'],
        'us': ['United States', 'US'],
        've': ['Venezuela', 'VE'],
        'pr': ['Puerto Rico', 'PR'],
        'bo': ['Bolivia', 'BO'],
        'rd': ['República Dominicana', 'RD']
    }

    print('Creando naciones...')

    for var, array in naciones_dict.items():
        var = Nacionalidad.objects.create()
        var.pais = array[0]
        var.abreviatura = array[1]
        var.save()


def main():
    crear_unidades()
    crear_rango()
    crear_rol()
    crear_clase()
    crear_naciones()


if __name__ == '__main__':
    main()
