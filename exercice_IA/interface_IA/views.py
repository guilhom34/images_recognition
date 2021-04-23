
import os
import pathlib
from datetime import datetime


from django.shortcuts import render
from django.http import HttpResponse


from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from interface_IA.common.training import predict_image
from interface_IA.forms import UploadFileForm

from .models import Images


def index(request):
    context = {
        'form': UploadFileForm()
    }
    return render(request, 'interface_IA/home_page.html', context)


def form_test(request):
    form = UploadFileForm(request.POST, request.FILES)
    file = request.FILES['file']
    res = predict_image(file)
    image = Images(datetime.now(), file.name, file.size, res)
    context = {
         'date': image.date,
         'size': image.size,
         'name': image.name,
         'result': image.result,
     }
    return render(request, 'interface_IA/image_list.html', context)

class ImagesDelete(DeleteView):
    model = Images
    fields = '__all__'
    template_name_suffix = '_delete'
    success_url = reverse_lazy('image_list')


class ImagesListView(ListView):
    model = Images
    fields = '__all__'
    template_name = 'interface_IA/image_list.html'

    def get_queryset(self):
        queryset = super(ImagesListView, self).get_queryset()
        return queryset
    # res = predict_image(file)
    # return HttpResponse(str(res))
