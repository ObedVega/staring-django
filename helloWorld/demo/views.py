from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1>Hello, world !!!</h1>")
    return render(request, 'demo/index.html')

def detail(request):
    return HttpResponse("<h1>Hello, world 2 !!!</h1>")

def mensaje(request):
    fullName = request.GET.get('fname', None)
    print("Nombre: "+fullName)
    respuesta = {'nombre':fullName}
    return render(request, 'demo/mensaje.html', respuesta)

