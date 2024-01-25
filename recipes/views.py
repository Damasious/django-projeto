from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, 'recipes/home.html')

def sobre(request):

    return HttpResponse('Sou o Fernando, tenho 31 anos')

def contato(request):

    return HttpResponse('TELEFONE: (11)983861290')