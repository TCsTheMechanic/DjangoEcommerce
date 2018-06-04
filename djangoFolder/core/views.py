# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    texts = ['texto 1', 'texto 2']
    context = {
        'title': 'django ecommerce',
        'texts': texts,
    }
    return render(request, 'index.html', context)
