from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from kosztorys.forms import KosztorysForm
from kosztorys.models import Kosztorys
from film.models import Film
# Create your views here.

def emp(request):
    '''Dodawanie nowego pracownika do bazy'''
    if request.method == "POST":
        form = KosztorysForm(request.POST)
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
                return redirect('/kosztorys/show')
            except:
                pass
    else:
        form = KosztorysForm()
    return render(request,'kosztorys/index.html',{'form':form})

def show(request):
    '''Wyswietlanie pracownikow'''
    kosztorysy = Kosztorys.objects.all()
    return render(request,"kosztorys/show.html",{'kosztorysy':kosztorysy})

def edit(request, id):
    '''Pozyskanie danych  istniejacego pracownika do edycji'''
    filmy = Film.objects.all()
    kosztorys = Kosztorys.objects.get(id=id)
    return render(request,'kosztorys/edit.html', {'kosztorys':kosztorys , 'filmy':filmy})

def update(request, id):
    '''Przeslanie nowych danych edytowanego pracownika '''
    kosztorys = Kosztorys.objects.get(id=id)
    form = KosztorysForm(request.POST, instance = kosztorys)
    if form.is_valid():
        form.save()
        return redirect("/kosztorys/show")
    return render(request, 'kosztorys/edit.html', {'kosztorys': kosztorys})

def destroy(request, id):
    '''Przekazanie id pracownika i usniecie go z bazy'''
    kosztorys = Kosztorys.objects.get(id=id)
    kosztorys.delete()
    return redirect("/kosztorys/show")
