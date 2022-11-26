from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from menadzer.forms import MenadzerForm
from menadzer.models import Menadzer
# Create your views here.

def emp(request):
    '''Dodawanie nowego pracownika do bazy'''
    if request.method == "POST":
        form = MenadzerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/menadzer/show')
            except:
                pass
    else:
        form = MenadzerForm()
    return render(request,'menadzer/index.html',{'form':form})

def show(request):
    '''Wyswietlanie pracownikow'''
    menadzerzy = Menadzer.objects.all()
    return render(request,"menadzer/show.html",{'menadzerzy':menadzerzy})

def edit(request, id):
    '''Pozyskanie danych  istniejacego pracownika do edycji'''
    menadzer = Menadzer.objects.get(id=id)
    return render(request,'menadzer/edit.html', {'menadzer':menadzer})

def update(request, id):
    '''Przeslanie nowych danych edytowanego pracownika '''
    menadzer = Menadzer.objects.get(id=id)
    form = MenadzerForm(request.POST, instance = menadzer)
    if form.is_valid():
        form.save()
        return redirect("/menadzer/show")
    return render(request, 'edit.html', {'menadzer': menadzer})

def destroy(request, id):
    '''Przekazanie id pracownika i usniecie go z bazy'''
    menadzer = Menadzer.objects.get(id=id)
    menadzer.delete()
    return redirect("/menadzer/show")
