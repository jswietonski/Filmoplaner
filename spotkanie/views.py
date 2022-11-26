from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from spotkanie.forms import SpotkanieForm
from spotkanie.models import Spotkanie
from film.models import Film
from studio.models import Studio
# Create your views here.

def emp(request):
    '''Dodawanie nowego pracownika do bazy'''
    if request.method == "POST":
        form = SpotkanieForm(request.POST)
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
                return redirect('/spotkanie/show')
            except:
                pass
    else:
        form = SpotkanieForm()
    return render(request,'spotkanie/index.html',{'form':form})

def show(request):
    '''Wyswietlanie pracownikow'''
    spotkania = Spotkanie.objects.all()
    return render(request, "spotkanie/show.html",{'spotkania':spotkania})

def edit(request, id):
    '''Pozyskanie danych  istniejacego pracownika do edycji'''
    studia = Studio.objects.all()
    filmy = Film.objects.all()
    spotkanie = Spotkanie.objects.get(id=id)
    return render(request, 'spotkanie/edit.html', {'spotkanie':spotkanie , 'studia':studia, 'filmy':filmy})

def update(request, id):
    '''Przeslanie nowych danych edytowanego pracownika '''
    spotkanie = Spotkanie.objects.get(id=id)
    form = SpotkanieForm(request.POST, instance = spotkanie)
    if form.is_valid():
        form.save()
        return redirect("/spotkanie/show")
    return render(request, 'spotkanie/edit.html', {'spotkanie': spotkanie})

def destroy(request, id):
    '''Przekazanie id pracownika i usniecie go z bazy'''
    spotkanie = Spotkanie.objects.get(id=id)
    spotkanie.delete()
    return redirect("/spotkanie/show")
