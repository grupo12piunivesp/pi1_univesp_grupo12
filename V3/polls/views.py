from django.shortcuts import render
from django import forms
from .models import *
from django.http import HttpResponse


from polls.forms import DoacaoForms,VoluntarioForms


# Define view de teste baseada em função (rotina para executar)
def index(request):
    return render (request, 'index.html')

#views para o frame polls/views.py
def sobre(request):
    return render (request, 'sobre.html')

def equipe(request):
    return render (request, 'equipe.html')

def doacoes_necessarias(request):

    if request.method == 'GET':
        
        form = DoacaoForms()

        context = {
            'form': form,
        }

        return render(request, 'doacoes_necessarias.html', context=context)
    
    else:

        form = DoacaoForms(request.POST)

        print(form.data['nome'])

        if form.is_valid():

            form.save()
            form = DoacaoForms()
    
        context = {
            'form': form,
            }
        
        return render(request, 'doacoes_necessarias.html', context=context)

def voluntario(request):

     if request.method == 'GET':
        
        form = VoluntarioForms()

        context = {
            'form': form,
        }

        return render(request, 'voluntario.html', context=context)
    
     else:

        form = VoluntarioForms(request.POST)

        print(form.data['nome'])

        if form.is_valid():

            form.save()
            form = VoluntarioForms()
    
        context = {
            'form': form,
            }
        
        return render(request, 'voluntario.html', context=context)

    #return render (request, 'voluntario.html')

def ajude(request):
    return render (request, 'ajude.html')