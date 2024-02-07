from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holamundo (request):
   
   c={
       'titulo':'hola',
       'mensaje':'como estas',
       'api':'ya estoy conectado',
       
       
   }

  
   template ='index.html'
   return render(request,template,c)

def home (request):
   template ='home.html'
   a = { 'nombre':'edwin diaz' ,'apellido':'Diaz' ,'direccion':'cayambe',}
   return render(request,template,a)


def apirest (request):
   template ='home.html'
   a = { 'nombre':'edwin diaz' ,'apellido':'Diaz' ,'direccion':'cayambe',}
   return render(request,template,a)
