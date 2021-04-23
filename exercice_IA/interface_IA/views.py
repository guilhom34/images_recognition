from datetime import datetime, timezone

from bson import ObjectId
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from interface_IA.common.training import predict_image
from interface_IA.forms import UploadFileForm

from .models import Image


def home_page(request):
    if request.method == 'GET':
        context = {
            'form': UploadFileForm()
        }
        return render(request, 'interface_IA/home_page.html', context)
    elif request.method == 'POST':
        file = request.FILES['file']
        res = predict_image(file)
        image = Image.objects.create(
            date=datetime.now(timezone.utc),
            name=file.name,
            size=file.size,
            result=res
        )
        context = {
            'form': UploadFileForm(),
            'image': image
        }
        return render(request, 'interface_IA/home_page.html', context)

class ImagesDelete(DeleteView):
    model = Image
    success_url = reverse_lazy('image_list')

    def get_object(self, queryset=None):
        query = Image.objects.filter(_id=ObjectId(oid=self.kwargs['pk']))
        return query.first()


class ImagesListView(ListView):
    model = Image

