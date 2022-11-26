from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from gatunek_filmu.forms import GatunekFilmuForm
from gatunek_filmu.models import GatunekFilmu
# Create your views here.

def emp(request):
    '''Dodawanie nowego pracownika do bazy'''
    if request.method == "POST":
        form = GatunekFilmuForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/gatunekfilmu/show')
            except:
                pass
    else:
        form = GatunekFilmuForm()
    return render(request,'gatunek_filmu/index.html',{'form':form})

def show(request):
    '''Wyswietlanie pracownikow'''
    gatunki = GatunekFilmu.objects.all()
    return render(request,"gatunek_filmu/show.html",{'gatunki':gatunki})

def edit(request, id):
    '''Pozyskanie danych  istniejacego pracownika do edycji'''
    gatunek = GatunekFilmu.objects.get(id=id)
    return render(request,'gatunek_filmu/edit.html', {'gatunek':gatunek})

def update(request, id):
    '''Przeslanie nowych danych edytowanego pracownika '''
    gatunek = GatunekFilmu.objects.get(id=id)
    form = GatunekFilmuForm(request.POST, instance = gatunek)
    if form.is_valid():
        form.save()
        return redirect("/gatunekfilmu/show")
    return render(request, 'gatunek_filmu/edit.html', {'gatunek':gatunek})

def destroy(request, id):
    '''Przekazanie id pracownika i usniecie go z bazy'''
    gatunek = GatunekFilmu.objects.get(id=id)
    gatunek.delete()
    return redirect("/gatunekfilmu/show")
