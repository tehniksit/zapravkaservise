#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from main.main_content.models import MainPage, TextRajony
from django.db.models import Q



def main_content(request):

    texts = MainPage.objects.all()

    context = {

        'texts':texts,
    }

    return render(request, 'main_content.html', context)

def contact_page(request):



    return render(request, 'contact_page.html', )


def about_us(request):



    return render(request, 'about_us.html', )


def rajony(request, rajony_id):



    rajony_content=TextRajony.objects.all()

    if int(rajony_id):


        rajony_content = TextRajony.objects.filter(

            Q(pk=rajony_id)
        )

    for rtitle in rajony_content:
        rtitle_1 = rtitle.title_rajony
        rtext_1 = rtitle.text_rajony

    context = {
        'rajony_content': rajony_content,
        'rajony_title': rtitle_1,
        'rajony_text': rtext_1,
    }

    return render(request, 'rajony.html', context)




