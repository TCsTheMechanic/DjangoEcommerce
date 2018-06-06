# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    texts = ['Aprendendo Django', 'May the force be with us']
    context = {
        'title': 'Django E-commerce',
        'texts': texts,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def productList(request):
    return render(request, 'productList.html')

def product(request):
    return render(request, 'product.html')
