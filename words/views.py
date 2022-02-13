from django.shortcuts import render
from .models import Word
# Create your views here.
from django.http import HttpResponse
def index(request):
    wordList = Word.objects.all()
    # wordList = Words.objects.raw("Select * from words;")
    return render(request, 'words/index.html', {'words': wordList})

def about(request):
    return render(request, 'words/about.html')

def hello(request):
    return render(request, 'words/hello.html')

def play(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html', {'message':'Please login to play'})
    else:
        return render(request, 'words/playGame.html')