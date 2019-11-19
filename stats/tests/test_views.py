from django.test import TestCase, Client
from django.urls import reverse
from stats.models import Clase, Rango, Nacionalidad, Rol, \
     Unidad, Miembro, Mision, Asistencia
import json
import os

print("Testeando views\n")
#TODO tenemos que hacer tests decentes

# class TestViews(TestCase):
#     def test_index_GET(self):
#         client = Client()

#         response = client.get(reverse('stats:index'))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'stats/index.html')

#     def test_lista_GET(self):
#         client = Client()

#         response = client.get(reverse('stats:stats-list'))

#         self.assertAlmostEquals(response.status_code, 200)
#         self.assertTemplateUsed((response, 'stats/tabla_asistencia.html'))

    # def test_upload_POST(self):

    #     client = Client()
    #     dir_script = os.path.dirname(os.path.realpath(__file__))
    #     test_file  = dir_script+'/reporte (2019-04-09).txt'

    #     with open(test_file) as t:
    #         reporte = t.readlines()

    #     response = client.post('stats/upload.html', reporte)
    #     self.assertAlmostEquals(response.status_code, 302)