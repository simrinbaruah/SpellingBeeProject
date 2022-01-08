from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request, 'words/index.html')

def about(request):
    return render(request, 'words/about.html')

def hello(request):
    return render(request, 'words/hello.html')