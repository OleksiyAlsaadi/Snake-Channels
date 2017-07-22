from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.
#@login_required(login_url="/login/")
def snake(request):
    #suggest = Suggestion(suggestion="test")
    #suggest.save()
    return render(request, 'snake.html')

def index(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            submit = form.cleaned_data['suggestion']
            num = form.cleaned_data['number']
            if (num <=0):
                #raise ValidationError("Must be over 0")
                for n in range(num,0):
                    Suggestion.objects.filter(suggestion=submit).delete()
                form = SuggestionForm()
            else:
                for n in range(0,num):
                    suggest = Suggestion(suggestion=submit)
                    suggest.save()
                form = SuggestionForm()
        else:
            submit = ""
    else:
        form = SuggestionForm()
        submit = ""
    first_bar = Suggestion.objects.all().filter(suggestion="X")
    second_bar = Suggestion.objects.filter(suggestion="O")
    context = {
        'title':"Home",
        'first': first_bar,
        'second': second_bar,
        'form':form,
        'submit':submit
        }
    return render(request,'home.html',context) #home

@csrf_exempt
def suggestions(request):
    if request.method == 'GET':
        suggestions = Suggestion.objects.all()
        suggest = {}
        suggest['suggestions']=[]
        for suggestion in suggestions:
            suggest['suggestions']+=[{
                'id':suggestion.id,
                'suggestion': suggestion.suggestion
                }]
        return JsonResponse(suggest)
    if request.method == 'POST':
        return HttpResponse("POST successful")
    return HttpResponse("404")
        # { 'suggestions':[
        #     {'id': id, 'suggestion': suggestion}
        # ]
        # }
