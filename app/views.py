from django.shortcuts import render, redirect
from .models import Laboratorio, DirectorGeneral, Producto

def index(request):
    
    return render(request, 'app/index.html')


def mostrar(request):
    laboratorios = Laboratorio.objects.all()
    
    return render(request, 'app/mostrar.html', {'laboratorios' : laboratorios})

def ingresar(request):
    
    if request.method == 'POST':
        
        try:
            nombre_labo = request.POST['nombre']
            pais_labo = request.POST['pais']
            ciudad_labo = request.POST['ciudad']
            
            if nombre_labo == '' or pais_labo == '' or ciudad_labo == '':
                raise ValueError
            
            lab = Laboratorio.objects.create(
                nombre=nombre_labo, 
                pais=pais_labo, 
                ciudad=ciudad_labo
            )
            
            lab.save()
        except ValueError as e:
            print('Error: hay que agregar datos validos')
    
    return render(request, 'app/ingresar.html', {})
    

def editar(request):
    lab_id = request.GET.get('id')
    lab_object = Laboratorio.objects.get(pk = lab_id)
    
    if request.method == 'POST':
        nombre_labo = request.POST['nombre']
        pais_labo = request.POST['pais']
        ciudad_labo = request.POST['ciudad']
        
        lab_object.nombre = nombre_labo
        lab_object.pais = pais_labo
        lab_object.ciudad = ciudad_labo
        
        lab_object.save()
    
    return render(request, 'app/editar.html', {'laboratorio' : lab_object})

def eliminar(request):
    lab_id = request.GET.get('id')
    lab_object = Laboratorio.objects.get(pk = lab_id)
    
    if request.method == 'POST':
        lab_object.delete()
        return redirect('mostrar')
    
    return render(request, 'app/eliminar.html', {'laboratorio' : lab_object})
    
