import datetime
from django import forms
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


CHOICES=[('select1','select 1'),
         ('select2','select 2')]

class Choice(models.Model):
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
