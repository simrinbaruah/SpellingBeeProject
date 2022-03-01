from django.shortcuts import render
from .models import Word, AudioStore
from gtts import gTTS
import random
from spellingbee import settings
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
        wordList = Word.objects.values('word')
        selected = random.choice(wordList)
        word = selected['word']
        request.session['selectedWord'] = word
        speech = gTTS(text=word, lang='en')
        fname = settings.MEDIA_ROOT+'\speech.mp3'
        try:
            previous_sound = AudioStore.objects.get(sound=fname)
            previous_sound.delete()
        except:
            pass
        speech.save(fname)

        audio_obj = AudioStore.objects.create(sound = fname)
        audio_obj.save()

        sound = AudioStore.objects.get(sound=fname)

        sendvals = {
            'sound' : sound
        }
        return render(request, 'words/playGame.html', {'sendvals': sendvals})

def option(request):
    if request.method == 'POST':
        selected_option = request.POST['dropdown']
        selected_word = request.session['selectedWord']
        # Word.objects.raw('Select '+ selected_option +' from words where word = "'+selected_word+'";')
        option_value = Word.objects.filter(word = selected_word).values(selected_option)
        option_value = option_value[0][selected_option]
        # print(option_value)
        speech = gTTS(text=option_value, lang='en')
        fname = settings.MEDIA_ROOT + '\speech.mp3'
        try:
            previous_sound = AudioStore.objects.get(sound=fname)
            previous_sound.delete()
        except:
            pass
        speech.save(fname)

        audio_obj = AudioStore.objects.create(sound=fname)
        audio_obj.save()

        sound = AudioStore.objects.get(sound=fname)

        sendvals = {
            'sound': sound
        }
        return render(request, 'words/playGame.html', {'sendvals': sendvals})
    return render(request, 'words/playGame.html')
