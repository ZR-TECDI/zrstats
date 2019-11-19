from django.test import SimpleTestCase
from django.urls import reverse, resolve
# from stats.views import index_view, upload_file, AsistenciaListView

print("Testeando URLs\n")
#TODO tenemos que hacer tests decentes, porque este no funciona bien

# class testUrls(SimpleTestCase):

#     def test_index_url_resolves(self):
#         url = reverse('stats:index')
#         self.assertEquals(resolve(url).func, index_view)

#     def test_upload_url_resolves(self):
#         url = reverse('stats:upload')
#         self.assertEquals(resolve(url).func, upload_file)

#     def test_list_url_resolves(self):
#         url = reverse('stats:stats-list')
#         self.assertEquals(resolve(url).func.view_class, AsistenciaListView)