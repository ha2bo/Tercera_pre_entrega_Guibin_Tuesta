from django.shortcuts import render
from .models import Sede

# Create your views here.


def inicio(req):

    return render(req, 'index.html', {})


def sobre_nosotros(req):

    return render(req, 'about.html', {})


#def servicios(req):
#
#    return render(req, 'service.html', {})


def contacto(req):

    return render(req, 'contact.html', {})

def sedes(req):

    lista_sedes = Sede.objects.all()

    #print(lista_sedes)

    return render(req, 'sedes.html', {'ListaSede' : lista_sedes})


def buscar(req):

    if req.GET["tipoDeSede"]:

        tipo_de_sede = req.GET["tipoDeSede"]
        lista_sedes =  Sede.objects.filter(tipo_gimnasio__icontains=tipo_de_sede)

        

    else:
        lista_sedes =  Sede.objects.filter(tipo_gimnasio__icontains=" ") #no pone nada
    
    return render(req, 'sedes.html', {'ListaSede' : lista_sedes})
