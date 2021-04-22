from django.shortcuts import render
from django.http import HttpResponse

from interface_IA.common.training import predict_image
from interface_IA.forms import UploadFileForm


def index(request):
    context = {
        'form': UploadFileForm()
    }
    return render(request, 'interface_IA/home_page.html', context)


def form_test(request):
    form = UploadFileForm(request.POST, request.FILES)
    file = request.FILES['file']
    res = predict_image(file)
    return HttpResponse(str(res))
