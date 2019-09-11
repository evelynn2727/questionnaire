from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def index(request):
   latest_question_list= Question.objects.order_by('-pub_date')[:5]
   template=loader.get_template('polls/index.html')
   context={'latest_question_list':latest_question_list,}
   return HttpResponse(template.render(context,request))

def detail(request, question_id):
   question= get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return HttpResponse(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
        # question.a_text = question.choice_set.get(pk=request.POST['choice'])
        # question.b_text = question.choice_set.get(pk=request.POST['choice'])
        # question.c_text = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice."
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        # question.a_text.votes+=1
        # question.a_text.save()
        # question.b_text.votes+=1
        # question.b_text.save()
        # question.c_text.votes+=1
        # question.c_text.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


