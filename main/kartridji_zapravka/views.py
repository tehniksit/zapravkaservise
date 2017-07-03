from django.core.paginator import Paginator, InvalidPage
from django.db.models import Q
from django.shortcuts import render
from main.kartridji_zapravka.form import *

def poisk_kartridj(request):


    return render(request, 'poisk_kartridj.html', locals() )

def result_of_poisk(request):
    poisk = request.GET.get("poisk")


    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1



    result_kartridjes = Zapravka.objects.all()

    if poisk:
        result_kartridjes = Zapravka.objects.filter(Q(long_name__icontains=poisk)|
                                                   Q(manufacturer__icontains=poisk)|
                                                   Q(short_name__icontains=poisk)|
                                                   Q(compatibility__name_dev__icontains=poisk)

                                                )

    paginator = Paginator(result_kartridjes, 8)

    current_page = int(page_num)

    try:
        result_kartridjes = paginator.page(page_num)
    except InvalidPage:
        result_kartridjes = paginator.page(1)


    context = {

        'result_kartridjes': result_kartridjes,
        'current_page': current_page,
        'poisk': poisk,


    }

    return render(request, 'result_of_poisk_kart.html', locals(), context)

def zapravka(request):
    cart_id = request.GET.get("cart_id")


    query_1 = Zapravka.objects.all()

    poisk = cart_id
    poisk = int(poisk)

    if poisk:

        query_1 = Zapravka.objects.filter(

            Q(id=poisk)
        )


    return render(request, 'kartridj_detail.html', locals() )

