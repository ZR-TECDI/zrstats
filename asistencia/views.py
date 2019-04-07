from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadReporteForm
from .ArmaStats import armastats
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def index_view(request):
    return render(request, 'asistencia/index.html', {})


def upload_file(request):
    if request.method == 'POST':
        form = UploadReporteForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            path = default_storage.save(str(file), ContentFile(file.read()))
            print(path)
            dict = armastats.main(path)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadReporteForm()
    return render(request, 'asistencia/upload.html', {'form': form})

