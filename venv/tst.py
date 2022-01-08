# import pyglet
# import os
# import winsound


# alter table sailors
# modify sid int  auto_increment;
# from gtts import gTTS
# sentence="Welcome to spelling bee"
# speech=gTTS(text=sentence, lang='en')
# speech.save('C:/Users/SIMRIN/OneDrive/Desktop/audiofiles/speech.wav')
# #os.system('start speech.mp3')
# winsound.PlaySound('C:/Users/SIMRIN/OneDrive/Desktop/audiofiles/speech.wav', winsound.SND_FILENAME)

# import pygame
# from gtts import gTTS
# from pygame import mixer
# import os

# sentence="Welcome to spelling bee"
# speech = gTTS(text=sentence, lang='en')
# speech.save('welcome.mp3')
#
# mixer.init()
# mixer.music.load('welcome.mp3')
# mixer.music.play()
# while mixer.music.get_busy():
#     continue
# mixer.music.unload()
# os.remove("welcome.mp3")


# from ctypes import *
# from ctypes import wintypes as w
#
# dll = WinDLL('winmm')
#
# dll.PlaySoundW.argtypes = w.LPCWSTR,w.HMODULE,w.DWORD
# dll.PlaySoundW.restype = w.BOOL
#
# SND_FILENAME = 0x20000
#
# # Call it with a Unicode string and it works.
# dll.PlaySoundW('speech.wav',None,SND_FILENAME)

# # import random
# # list1=[1,2,3,4]
# #
# # selected=random.choice(list1)
# # print(selected)
# #
# # print(list)
# # for i in list:
# #     print(i)
#
# # name="Nikki"
# # score=25.655
# # print("Hello, my name is %s. My score is %.2f" %(name, score))
# #
# # num=10
# # print(type(num))
# #
# # convert="%s" %(num)
# # print(type(convert))
# #
# #
# # person=[(1, 'Nikki'), (2, 'Alex'), (3, 'Arav')]
# #
# # for id,name in person:
# #     print("id: %d" %(id))
# #     print("name: %s" %(name))
# #
# #
# # name="Nikki"
# # if(type(name)==str):
# #     print("string")
# # if(isinstance(name, str)==True):
# #     print("string1")
#
# # x="nikki"
# # try:
# #     print(x)
# #     f=open("test.txt")
# # except NameError:
# #     print("Sorry. x needs to be defined first.")
# # except Exception as e:
# #     print(e)
#
# # a=dict(zip("a", "1"))
# # print(a)
#

#https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    audio=r.listen(source)

try:
    text = r.recognize_google(audio)
    print ("you said: " + text)
    print(type(text))
    text=text.replace(" ", "")
    print(text)
    # error occurs when google could not understand what was said

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")