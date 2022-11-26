"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pracownik import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from homepage import  views as views_homepage
from menadzer import views as views_menadzer
from gatunek_filmu import  views as views_gatunki
from studio import  views as views_studio
from aktor import views as views_aktor
from film import views as views_film
from spotkanie import views as views_spotkanie
from kosztorys import  views as views_kosztorys
from zadanie import views as views_zadanie
from rola import views as views_rola

urlpatterns = [
    path('',views_homepage.render_homepage),
    path('admin/doc/',include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("homepage/", views_homepage.render_homepage),
    path('menadzer/emp', views_menadzer.emp),
    path('menadzer/show',views_menadzer.show),
    path('menadzer/edit/<int:id>', views_menadzer.edit),
    path('menadzer/update/<int:id>', views_menadzer.update),
    path('menadzer/delete/<int:id>', views_menadzer.destroy),
    path('gatunekfilmu/emp', views_gatunki.emp),
    path('gatunekfilmu/show', views_gatunki.show),
    path('gatunekfilmu/edit/<int:id>', views_gatunki.edit),
    path('gatunekfilmu/update/<int:id>', views_gatunki.update),
    path('gatunekfilmu/delete/<int:id>', views_gatunki.destroy),
    path('studio/emp', views_studio.emp),
    path('studio/show', views_studio.show),
    path('studio/edit/<int:id>', views_studio.edit),
    path('studio/update/<int:id>', views_studio.update),
    path('studio/delete/<int:id>', views_studio.destroy),
    path('aktor/emp', views_aktor.emp),
    path('aktor/show', views_aktor.show),
    path('aktor/edit/<int:id>', views_aktor.edit),
    path('aktor/update/<int:id>', views_aktor.update),
    path('aktor/delete/<int:id>', views_aktor.destroy),
    path('film/emp', views_film.emp),
    path('film/show', views_film.show),
    path('film/edit/<int:id>', views_film.edit),
    path('film/update/<int:id>', views_film.update),
    path('film/delete/<int:id>', views_film.destroy),
    path('spotkanie/emp', views_spotkanie.emp),
    path('spotkanie/show', views_spotkanie.show),
    path('spotkanie/edit/<int:id>', views_spotkanie.edit),
    path('spotkanie/update/<int:id>', views_spotkanie.update),
    path('spotkanie/delete/<int:id>', views_spotkanie.destroy),
    path('kosztorys/emp', views_kosztorys.emp),
    path('kosztorys/show', views_kosztorys.show),
    path('kosztorys/edit/<int:id>', views_kosztorys.edit),
    path('kosztorys/update/<int:id>', views_kosztorys.update),
    path('kosztorys/delete/<int:id>', views_kosztorys.destroy),
    path('zadanie/emp', views_zadanie.emp),
    path('zadanie/show', views_zadanie.show),
    path('zadanie/edit/<int:id>', views_zadanie.edit),
    path('zadanie/update/<int:id>', views_zadanie.update),
    path('zadanie/delete/<int:id>', views_zadanie.destroy),
    path('rola/emp', views_rola.emp),
    path('rola/show', views_rola.show),
    path('rola/edit/<int:id>', views_rola.edit),
    path('rola/update/<int:id>', views_rola.update),
    path('rola/delete/<int:id>', views_rola.destroy),

]
urlpatterns += staticfiles_urlpatterns()
