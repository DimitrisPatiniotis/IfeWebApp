from django.shortcuts import render


# Create your views here.
def analysisView(request):
    return render(request, 'subject-analysis.html')

def homeView(request):
    return render(request, 'home.html')