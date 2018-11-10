# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render , redirect

from .forms import produitform
from siteweb.models import Articles
# Create your views here.

def form(request):
    articles = Articles.objects.all().order_by('prix')
    return render(request,'form.html',locals());

def home(request):

    form = produitform(request.POST)
    if form.is_valid():
        nom_produit = form.cleaned_data['nom_produit']
        quantite = form.cleaned_data['quantite']
        prix = form.cleaned_data['prix']
        form.save()


    return render(request,'index.html',locals());

#
