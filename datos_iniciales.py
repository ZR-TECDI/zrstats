"""Agrega los datos iniciales de forma automática"""

from stats.models import *
from collections import defaultdict
import os


lista = [Miembro, Rango, Unidad, Rol, Nacionalidad, Clase]
for item in lista:
    item.objects.all().delete()


def crear_unidades():
    unidades_dict = {
        'altm': ['Alto Mando', 'ALTM'],
        'infm': ['Inf. de Marines', 'IMZR'],
        'paraca': ['Paracaidistas', 'PAR'],
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
        'leb': ['Líder Equipo B', 'LEB'],
        'a':['ALPHA', 'A'],
        'b':['BRAVO', 'B'],
        'cmda1':['Com. Ariete 1', 'CMDA1'],
        'cmda2':['Com. Ariete 2', 'CMDA2'],
        'cmda3':['Com. Ariete 3', 'CMDA3'],
        'cmda4':['Com. Ariete 4', 'CMDA4']
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
        'co': ['Colombia', 'CO'],
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
        'rd': ['República Dominicana', 'RD'],
        'ca': ['Canadá', 'CA']
    }

    print('Creando naciones...')

    for var, array in naciones_dict.items():
        var = Nacionalidad.objects.create()
        var.pais = array[0]
        var.abreviatura = array[1]
        var.save()


def agregar_miembros():
    #rango|nombre|clase1|clase2|nac|est|unidad|pel|esc|rol
    # 0      1      2     3      4   5     6    7   8   9

    script_dir = os.path.dirname(os.path.realpath(__file__))
    datos_iniciales = script_dir + '\\datos_iniciales.txt'
    with open(datos_iniciales) as txt:
        for line in txt.readlines():
            array = line.replace('\n', '').split(' ')
            print(array)
            user = User.objects.create_user(username=array[1], email=array[1]+"@zrarmy.com", password=array[1].lower())
            miembro = Miembro.objects.get(nombre=array[1])
            miembro.nombre = array[1]
            print(miembro.nombre)
            miembro.rango = Rango.objects.get(abreviatura = array[0])
            print(miembro.rango)
            miembro.clase1 = Clase.objects.get(abreviatura = array[2])
            print(miembro.clase1)
            miembro.clase2 = Clase.objects.get(abreviatura = array[3])
            print(miembro.clase2)
            miembro.nacionalidad = Nacionalidad.objects.get(abreviatura = array[4])
            print(miembro.nacionalidad)

            if array[5] == 'A':
                el_estado = 'Activo'
            elif array[5] == 'R':
                el_estado = 'Reserva'
            miembro.estado = el_estado
            print(miembro.estado)

            miembro.unidad = Unidad.objects.get(abreviatura = array[6])
            print(miembro.unidad)
            miembro.peloton = array[7]
            print(miembro.peloton)
            miembro.escuadra = array[8]
            print(miembro.escuadra)
            miembro.rol = Rol.objects.get(abreviatura = array[9])
            print(miembro.rol)
            miembro.save()
            if miembro.nombre == "Admin":
                user.is_staff = True
                user.is_superuser = True
                user.save()
            print(miembro)


def main():
    crear_unidades()
    crear_rango()
    crear_rol()
    crear_clase()
    crear_naciones()
    agregar_miembros()
    print("FINALIZADO DATOS INICIALES")


if __name__ == '__main__':
    main()
