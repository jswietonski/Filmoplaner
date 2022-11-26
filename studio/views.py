from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from studio.forms import StudioForm
from studio.models import Studio
# Create your views here.

def emp(request):
    '''Dodawanie nowego pracownika do bazy'''
    if request.method == "POST":
        form = StudioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/studio/show')
            except:
                pass
    else:
        form = StudioForm()
    return render(request,'studio/index.html',{'form':form})

def show(request):
    '''Wyswietlanie pracownikow'''
    studia = Studio.objects.all()
    return render(request,"studio/show.html",{'studia':studia})

def edit(request, id):
    '''Pozyskanie danych  istniejacego pracownika do edycji'''
    studio = Studio.objects.get(id=id)
    return render(request,'studio/edit.html', {'studio':studio})

def update(request, id):
    '''Przeslanie nowych danych edytowanego pracownika '''
    studio = Studio.objects.get(id=id)
    form = StudioForm(request.POST, instance = studio)
    if form.is_valid():
        form.save()
        return redirect("/studio/show")
    return render(request, 'studio/edit.html', {'studio':studio})

def destroy(request, id):
    '''Przekazanie id pracownika i usniecie go z bazy'''
    studio = Studio.objects.get(id=id)
    studio.delete()
    return redirect("/studio/show")
