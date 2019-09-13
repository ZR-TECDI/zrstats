from django.test import TestCase, Client
from django.urls import reverse
from asistencia.models import Clase, Rango, Nacionalidad, Rol, \
     Unidad, Miembro, Mision, Asistencia
import json
import os

print("Testeando views\n")

class TestViews(TestCase):
    def test_index_GET(self):
        client = Client()

        response = client.get(reverse('asistencia:index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'asistencia/index.html')

    def test_lista_GET(self):
        client = Client()

        response = client.get(reverse('asistencia:asistencia-list'))

        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed((response, 'asistencia/tabla_asistencia.html'))

    # def test_upload_POST(self):
#TODO necesitamos testear este método, qué data recibe el post?

    #     client = Client()
    #     dir_script = os.path.dirname(os.path.realpath(__file__))
    #     test_file  = dir_script+'/reporte (2019-04-09).txt'

    #     with open(test_file) as t:
    #         reporte = t.readlines()

    #     response = client.post('asistencia/upload.html', reporte)
    #     self.assertAlmostEquals(response.status_code, 302)