from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
import tabula
import pandas as pd

def handle_uploaded_file(f):
    with open('', 'wb+') as destination:
        pass

# Create your views here.
def analysisView(request):
    if request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']
        data = tabula.read_pdf(uploaded_file, pages='all')[0]
        # data.to_csv('out.csv', sep='\t', encoding='utf-8')
        print(data)
        # fs = FileSystemStorage()
        # name = fs.save(uploaded_file.name, uploaded_file)
        # uploaded_file_url = fs.url(name)
        # context['uploaded_file_url'] = fs.url(name)

        return render(request, 'subject-analysis.html')

    else:
        return render(request, 'subject-analysis.html')


def homeView(request):
    return render(request, 'home.html')