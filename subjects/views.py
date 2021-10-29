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
        return render(request, 'subject-analysis.html')


def homeView(request):
    return render(request, 'home.html')