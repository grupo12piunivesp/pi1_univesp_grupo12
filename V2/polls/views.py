from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define view de teste baseada em função (rotina para executar)
def index(request):
    return render (request, 'index.html')

#views para o frame polls/views.py
def sobre(request):
    return render (request, 'sobre.html')

def equipe(request):
    return render (request, 'equipe.html')

def doacoes_necessarias(request):
    return render (request, 'doacoes_necessarias.html')

def voluntario(request):
    return render (request, 'voluntario.html')

def ajude(request):
    return render (request, 'ajude.html')