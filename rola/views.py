from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from rola.forms import RolaForm
from rola.models import Rola
from film.models import Film
from aktor.models import Aktor
# Create your views here.

def emp(request):
    '''Dodawanie nowego pracownika do bazy'''
    if request.method == "POST":
        form = RolaForm(request.POST)
        #film = Film

        if form.is_valid():
            try:
                form.save()
                return redirect('/rola/show')
            except:
                pass
    else:
        form = RolaForm()
    return render(request,'rola/index.html',{'form':form})

def show(request):
    '''Wyswietlanie pracownikow'''
    role = Rola.objects.all()
    return render(request, "rola/show.html",{'role':role})

def edit(request, id):
    '''Pozyskanie danych  istniejacego pracownika do edycji'''
    aktorzy = Aktor.objects.all()
    filmy = Film.objects.all()
    rola = Rola.objects.get(id=id)
    return render(request, 'rola/edit.html', {'rola':rola , 'aktorzy':aktorzy, 'filmy':filmy})

def update(request, id):
    '''Przeslanie nowych danych edytowanego pracownika '''
    rola = Rola.objects.get(id=id)
    form = RolaForm(request.POST, instance = rola)
    if form.is_valid():
        form.save()
        return redirect("/rola/show")
    return render(request, 'rola/edit.html', {'rola': rola})

def destroy(request, id):
    '''Przekazanie id pracownika i usniecie go z bazy'''
    rola = Rola.objects.get(id=id)
    rola.delete()
    return redirect("/rola/show")
