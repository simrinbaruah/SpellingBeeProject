import mysql.connector
import random
import os
from gtts import gTTS
import pygame
from pygame import mixer
import speech_recognition as sr


def play_audio(sentence):
    speech=gTTS(text=sentence, lang='en')
    speech.save('speech.mp3')
    mixer.init()
    mixer.music.load('speech.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        continue
    mixer.music.unload()
    os.remove("speech.mp3")


spelling=mysql.connector.connect(
    host="localhost",
    username="root",
    password="simrin",
    database="spelling"
)
cursor=spelling.cursor()
# sql="CREATE TABLE words(" \
#     "word_id int, " \
#     "word VARCHAR(100)," \
#     "definition TEXT," \
#     "example_1 TEXT," \
#     "example_2 TEXT," \
#     "origination VARCHAR(50))"

# sql="CREATE TABLE users(" \
#     "user_id int primary key, " \
#     "username varchar(100), " \
#     "password varchar(100))"

# sql="ALTER TABLE users " \
#     "MODIFY username varchar(100) UNIQUE "
#
# cursor.execute(sql)

# sql="CREATE TABLE scores(" \
#     "score_id int primary key, " \
#     "user_id int, " \
#     "correct int, " \
#     "incorrect int, " \
#     "foreign key (user_id) references users(user_id))"


# # sql="INSERT INTO words VALUES(%s, %s, %s, %s, %s, %s, %s)"
# # list1=[]
# # while True:
# #     try:
# #         a=int(input("word_id: "))
# #     except ValueError:
# #         print("Incorrect Syntax")
# #         break
# #     b=input("word: ")
# #     c=input("definition: ")
# #     d=input("example 1: ")
# #     e=input("example 2: ")
# #     f=input("origination: ")
# #     g=input("part of speech: ")
# #     tup=(a,b,c,d,e,f,g)
# #     list1.append(tup)
# #
# #
# # cursor.executemany(sql,list1)
# # spelling.commit()

uname=input("Username: ")
sql="SELECT username FROM users where username=%s"
values=(uname,)
cursor.execute(sql,values)
userExists=cursor.fetchone()
if(userExists):
    pswd=input("Password: ")
    sql="SELECT username, password FROM users where username=%s and password=%s"
    values=(uname, pswd)
    cursor.execute(sql,values)
    user=cursor.fetchone()
    if(user):
        welcome = "Welcome to spelling bee."
        play_audio(welcome)

        sql = "SELECT * FROM words"
        cursor.execute(sql)
        list2 = cursor.fetchall()

        exitgame=0
        while exitgame!=1:
            selected = random.choice(list2)
            print(selected)
            spell = "Please spell " + selected[1]
            while True:
                play_audio(spell)
                options = input("Options"
                                "\n1.Repeat the word"
                                "\n2.Definition"
                                "\n3.Example 1"
                                "\n4.Example 2"
                                "\n5.Origination"
                                "\n6.Part Of Speech"
                                "\n7.Exit Game"
                                "\nSpell the word? ")
                if (options.isdigit()):
                    if (int(options) == 1):
                        play_audio(spell)
                    elif (int(options) == 7):
                        exitgame=1
                        break
                    else:
                        play_audio(selected[int(options)])

                elif options.lower() == selected[1]:
                    play_audio('Correct')
                    break
                else:
                    play_audio("Sorry. Wrong answer.")
                    break

    else:
        print("Wrong password")
else:
    print("Username does not exist")

# uname=input("Enter username: ")
# sql="SELECT username FROM users WHERE username=%s"
# values=(uname,)
# cursor.execute(sql, values)
# username=cursor.fetchone()
# if(username):
#     pwd = input("Enter password: ")
#     sql="SELECT user_id FROM users WHERE username=%s AND password=%s"
#     values=(uname, pwd)
#
#     cursor.execute(sql, values)
#
#     userID=cursor.fetchone()
#
#     if(userID):
#
#         welcome = "Welcome to spelling bee."
#         play_audio(welcome)
#
#         sql = "SELECT * FROM words"
#         cursor.execute(sql)
#         list2 = cursor.fetchall()
#
#         score_correct=0
#         score_incorrect=0
#         exitgame=0
#
#         while(exitgame!=1):
#             if(len(list2)==0):
#                 print("No more words available.")
#                 break
#             selected = random.choice(list2)
#             print(selected)
#             spell = "Please spell " + selected[1]
#             play_audio(spell)
#             while True:
#                 options = input("Options"
#                                 "\n1.Repeat the word"
#                                 "\n2.Definition"
#                                 "\n3.Example 1"
#                                 "\n4.Example 2"
#                                 "\n5.Origination"
#                                 "\n6.Part Of Speech"
#                                 "\n7.Exit Game"
#                                 "\nSpell the word? ")
#                 if (options.isdigit()):
#                     if (int(options) == 1):
#                         play_audio(spell)
#                     elif (int(options) == 7):
#                         exitgame=1
#                         break
#                     else:
#                         play_audio(selected[int(options)])
#                 elif options.lower() == selected[1]:
#                     play_audio('Correct')
#                     score_correct=score_correct+1
#                     list2.remove(selected)
#                     break
#                 else:
#                     play_audio("Sorry. Wrong answer.")
#                     score_incorrect=score_incorrect+1
#                     break
#
#         total=score_correct-score_incorrect
#         print("Score: ", total)
#         print("Correct: ", score_correct)
#         print("Incorrect: ", score_incorrect)
#
#         sql="INSERT INTO scores values(1, %s, %s, %s)"
#         values=(userID[0], score_correct, score_incorrect)
#
#         cursor.execute(sql, values)
#         spelling.commit()
#     else:
#         print("Incorrect Password.")
# else:
#     print("Username "+uname+" does not exist.")


