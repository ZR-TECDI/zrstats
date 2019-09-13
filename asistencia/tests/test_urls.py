from django.test import SimpleTestCase
from django.urls import reverse, resolve
from asistencia.views import index_view, upload_file, AsistenciaListView

print("Testeando URLs\n")

class testUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('asistencia:index')
        self.assertEquals(resolve(url).func, index_view)

    def test_upload_url_resolves(self):
        url = reverse('asistencia:upload')
        self.assertEquals(resolve(url).func, upload_file)

    def test_list_url_resolves(self):
        url = reverse('asistencia:asistencia-list')
        self.assertEquals(resolve(url).func.view_class, AsistenciaListView)