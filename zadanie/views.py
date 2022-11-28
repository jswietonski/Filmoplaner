from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from zadanie.forms import ZadanieForm
from zadanie.models import Zadanie
from pracownik.models import Pracownik
from menadzer.models import Menadzer
from film.models import Film
# Create your views here.

def emp(request):
    '''Dodawanie nowego zadania do bazy'''
    if request.method == "POST":
        form = ZadanieForm(request.POST)
        #film = Film

        if form.is_valid():
            try:
                #film(nazwa=form.cleaned_data['nazwa'],
                    # budzet=form.cleaned_data['budzet'],
                    # id_gatunek=form.cleaned_data['id_gatunek'],
                    # ograniczenie_wiekowe=form.cleaned_data['ograniczenie_wiekowe'],
                    # data_premiery=form.cleaned_data['data_premiery'])
                #film.save()
                form.save()
                return redirect('/zadanie/show')
            except:
                pass
    else:
        form = ZadanieForm()
    return render(request,'zadanie/index.html',{'form':form})

def show(request):
    '''Wyswietlanie zadani'''
    zadania = Zadanie.objects.all()
    return render(request,"zadanie/show.html",{'zadania':zadania})

def edit(request, id):
    '''Pozyskanie danych  istniejacego zadania do edycji'''
    filmy = Film.objects.all()
    pracownicy = Pracownik.objects.all()
    menadzerzy = Menadzer.objects.all()
    zadanie = Zadanie.objects.get(id=id)
    return render(request,'zadanie/edit.html', {'zadanie':zadanie, 'filmy':filmy, 'pracownicy':pracownicy, 'menadzerzy':menadzerzy})

def update(request, id):
    '''Przeslanie nowych danych edytowanego zadania '''
    zadanie = Zadanie.objects.get(id=id)
    form = ZadanieForm(request.POST, instance = zadanie)
    if form.is_valid():
        form.save()
        return redirect("/zadanie/show")
    return render(request, 'zadanie/edit.html', {'zadanie': zadanie})

def destroy(request, id):
    '''Przekazanie id zadania i usniecie go z bazy'''
    zadanie = Zadanie.objects.get(id=id)
    zadanie.delete()
    return redirect("/zadanie/show")
