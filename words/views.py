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
        request.session['score'] = 0
        request.session['wordList'] = list(wordList)
        sound = convertAudio(word)
        sendvals = {
            'sound' : sound
        }
        return render(request, 'words/playGame.html', {'sendvals': sendvals})

def option(request):
    if request.method == 'POST':
        selected_option = request.POST['dropdown']
        selected_word = request.session['selectedWord']
        if selected_option == 'repeat':
            selected_option = 'word'
        # Word.objects.raw('Select '+ selected_option +' from words where word = "'+selected_word+'";')
        option_value = Word.objects.filter(word = selected_word).values(selected_option)
        option_value = option_value[0][selected_option]
        # print(option_value)
        sound = convertAudio(option_value)
        sendvals = {
            'sound': sound
        }
        return render(request, 'words/playGame.html', {'sendvals': sendvals})
    return render(request, 'words/playGame.html')

def check(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        word = request.session['selectedWord']
        result = 'Wrong Answer!'
        if word.lower() == answer.lower():
            result = 'Correct Answer!'
            request.session['score'] += 1
        wordList = request.session['wordList']
        selected = random.choice(wordList)
        word = selected['word']
        request.session['selectedWord'] = word
        score = request.session['score']
        sound = convertAudio(word)
        sendvals = {
            'sound': sound,
            'result' : result,
            'score' : score
        }
        return render(request, 'words/playGame.html', {'sendvals':sendvals})


def convertAudio(sentence):
    speech = gTTS(text=sentence, lang='en')
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
    return sound