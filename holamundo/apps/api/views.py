from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def holamundo (request):
   
   c:{}
   c['titulo'] = 'hola mundo'
   template ='index.html'
   return render(request,template,c)

def home (request):
    return HttpResponse('hola home')