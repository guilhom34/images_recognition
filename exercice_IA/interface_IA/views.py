import os
import pathlib

from django.shortcuts import render
from django.http import HttpResponse
import uuid
from interface_IA.forms import UploadFileForm

from common.training import prediction


def index(request):
    context = {
        'form': UploadFileForm()
    }
    return render(request, 'interface_IA/home_page.html', context)


def form_test(request):
    form = UploadFileForm(request.POST, request.FILES)
    file = request.FILES['file']
    extension = pathlib.PureWindowsPath(file.name).suffix
    file_name = str(uuid.uuid4()) + extension
    file_path = os.getcwd() + '//temp//' + file_name
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    res = prediction(file_path)
    print(res)
    return HttpResponse("Hello, world. You're at the polls index.")
