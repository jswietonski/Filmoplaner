from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from film.forms import FilmForm
from film.models import Film
from gatunek_filmu.models import GatunekFilmu
# Create your views here.

def emp(request):
    '''Dodawanie nowego filmu do bazy'''
    if request.method == "POST":
        form = FilmForm(request.POST)
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
                return redirect('/film/show')
            except:
                pass
    else:
        form = FilmForm()
    return render(request,'film/index.html',{'form':form})

def show(request):
    '''Wyswietlanie filmów'''
    filmy = Film.objects.all()
    return render(request,"film/show.html",{'filmy':filmy})

def edit(request, id):
    '''Pozyskanie danych  istniejacego filmu do edycji'''
    gatunki = GatunekFilmu.objects.all()
    film = Film.objects.get(id=id)
    return render(request,'film/edit.html', {'film':film , 'gatunki':gatunki})

def update(request, id):
    '''Przeslanie nowych danych edytowanego filmu '''
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST, instance = film)
    if form.is_valid():
        form.save()
        return redirect("/film/show")
    return render(request, 'film/edit.html', {'film': film})

def destroy(request, id):
    '''Przekazanie id filmu i usniecie go z bazy'''
    film = Film.objects.get(id=id)
    film.delete()
    return redirect("/film/show")
