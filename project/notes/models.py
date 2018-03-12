from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Note(models.Model):
    note_heading = models.CharField(max_length=100, default=' ')
    note_text = models.CharField(max_length=700)
    pub_date = models.DateTimeField('date added')

    def __str__(self):
        return self.note_heading

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __srt__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text