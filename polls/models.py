import datetime
from django import forms
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #choice fields
    a_text= models.CharField(max_length=200, default=0)
    b_text= models.CharField(max_length=200, default=0)
    c_text= models.CharField(max_length=200, default=0)
    CHOICE=[(a_text, b_text, c_text)]
    #################
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    ##############################
    def __str__(self):
        return self.a_text
    def __str__(self):
        return self.b_text
    def __str__(self):
        return self.c_text
    #########################
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
