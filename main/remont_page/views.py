#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render



def remont_page(request):
    var = 'Hello world'
    context = {
        'var': var,
    }

    return render(request, 'content_page.html', context)




