# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
# from django.urls import reverse
#
# # from landing.form import *
# from django.db.models import Q
# from django.forms import modelform_factory
# from django.core.paginator import Paginator, InvalidPage
from main.skup.models import HP, Brother, Kyocera, Canon, Samsung

def zakup(request):



    return render(request, 'skupka/base_skupka.html', )
def zakup_hp(request):
    texts = HP.objects.all()

    context = {

        'texts': texts,
    }

    return render(request, 'skupka/price_hp.html', context )
def zakup_brother(request):
    texts = Brother.objects.all()

    context = {

        'texts': texts,
    }
    return render(request, 'skupka/price_brother.html', context )
def zakup_kyocera(request):
    texts = Kyocera.objects.all()

    context = {

        'texts': texts,
    }
    return render(request, 'skupka/price_kyocera.html', context)
def zakup_canon(request):
    texts = Canon.objects.all()

    context = {

        'texts': texts,
    }
    return render(request, 'skupka/price_canon.html', context)
def zakup_samsung(request):
    texts = Samsung.objects.all()

    context = {

        'texts': texts,
    }
    return render(request, 'skupka/price_samsung.html', context )