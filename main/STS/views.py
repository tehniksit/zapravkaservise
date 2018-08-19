# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
# from django.urls import reverse
#
# # from landing.form import *
# from django.db.models import Q
# from django.forms import modelform_factory
# from django.core.paginator import Paginator, InvalidPage


def about(request):

    return render(request, 'sts/smart-toner-system.html')


def sts_vo(request):

    return render(request, 'sts/sts_v-o.html')
def sts_howitworks(request):

    return render(request, 'sts/sts_princip.html')
def sts_supply(request):

    return render(request, 'sts/sts_supply.html')
def sts_price(request):

    return render(request, 'sts/sts_price.html')



