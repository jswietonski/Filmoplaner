from django.shortcuts import render

from django.shortcuts import render, redirect
from pracownik.forms import PracownikForm
from pracownik.models import Pracownik
# Create your views here.

def emp(request):
    '''Dodawanie nowego pracownika do bazy'''
    if request.method == "POST":
        form = PracownikForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = PracownikForm()
    return render(request,'index.html',{'form':form})

def show(request):
    '''Wyswietlanie pracownikow'''
    pracownicy = Pracownik.objects.all()
    return render(request,"show.html",{'pracownicy':pracownicy})

def edit(request, id):
    '''Pozyskanie danych  istniejacego pracownika do edycji'''
    pracownik = Pracownik.objects.get(id=id)
    return render(request,'edit.html', {'pracownik':pracownik})

def update(request, id):
    '''Przeslanie nowych danych edytowanego pracownika '''
    pracownik = Pracownik.objects.get(id=id)
    form = PracownikForm(request.POST, instance = pracownik)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'pracownik': pracownik})

def destroy(request, id):
    '''Przekazanie id pracownika i usniecie go z bazy'''
    pracownik = Pracownik.objects.get(id=id)
    pracownik.delete()
    return redirect("/show")
