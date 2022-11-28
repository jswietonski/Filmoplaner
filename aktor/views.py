from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render, redirect
from aktor.forms import AktorForm
from aktor.models import Aktor
# Create your views here.

def emp(request):
    '''Dodawanie nowego aktora do bazy'''
    if request.method == "POST":
        form = AktorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/aktor/show')
            except:
                pass
    else:
        form = AktorForm()
    return render(request,'aktor/index.html',{'form':form})

def show(request):
    '''Wyswietlanie aktorów'''
    aktorzy = Aktor.objects.all()
    return render(request,"aktor/show.html",{'aktorzy':aktorzy})

def edit(request, id):
    '''Pozyskanie danych  istniejacego aktora do edycji'''
    aktor = Aktor.objects.get(id=id)
    return render(request,'aktor/edit.html', {'aktor':aktor})

def update(request, id):
    '''Przeslanie nowych danych edytowanego aktora '''
    aktor = Aktor.objects.get(id=id)
    form = AktorForm(request.POST, instance = aktor)
    if form.is_valid():
        form.save()
        return redirect("/aktor/show")
    return render(request, 'edit.html', {'aktor': aktor})

def destroy(request, id):
    '''Przekazanie id aktora i usniecie go z bazy'''
    aktor = Aktor.objects.get(id=id)
    aktor.delete()
    return redirect("/aktor/show")
