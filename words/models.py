# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=100, blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    example_1 = models.TextField(blank=True, null=True)
    example_2 = models.TextField(blank=True, null=True)
    origination = models.CharField(max_length=50, blank=True, null=True)
    part_of_speech = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'words'


class AudioStore(models.Model):
    sound = models.FileField(upload_to='\documents')

    def __str__(self):
        return 'SOUND'


class Score(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class CorrectWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=100, blank=True, null=True)
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)