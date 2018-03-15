from django.db import models
from django.contrib.auth.models import User


# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

#Hardcore

#Hope that Hardcore ends


class Note(models.Model):

    note_heading = models.CharField(max_length=100, default=' ')
    note_text = models.TextField(max_length=700)
    pub_date = models.DateTimeField('date added', default= datetime.datetime.now())
    pub_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pub_author.username) + '  .....  ' + self.note_heading

    def __repr__(self):
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

