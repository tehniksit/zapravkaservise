from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from main.kartridji_zapravka.form import *

def poisk_kartridj(request):


    return render(request, 'poisk_kartridj.html', locals() )

def result_of_poisk(request):
    # poisk = request.GET.get("poisk")
    #
    #
    # try:
    #     page_num = request.GET["page"]
    # except KeyError:
    #     page_num = 1
    #
    #
    #
    # result_kartridjes = Zapravka.objects.all()
    #
    # if poisk:
    #     result_kartridjes = Zapravka.objects.filter(Q(long_name__icontains=poisk)|
    #                                                # Q(manufacturer__icontains=poisk)|
    #                                                Q(short_name__icontains=poisk)
    #                                                # Q(compatibility__name_dev__icontains=poisk)
    #
    #                                             )
    #
    # paginator = Paginator(result_kartridjes, 8)
    #
    # current_page = int(page_num)
    #
    # try:
    #     result_kartridjes = paginator.page(page_num)
    # except PageNotAnInteger:
    #
    #     result_kartridjes = paginator.page(1)
    # except EmptyPage:
    #
    #     result_kartridjes = paginator.page(paginator.num_pages)
    #
    #
    # context = {
    #
    #     'result_kartridjes': result_kartridjes,
    #     'current_page': current_page,
    #     'poisk': poisk,
    #
    #
    # }

    view_w = request.GET.get("view_w")
    view_in = request.GET.get("view_in")

    manufacturer = request.GET.get("manufacturer")

    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1

    result_kartridjes = Zapravka.objects.all()

    if manufacturer:
        result_kartridjes = Zapravka.objects.filter(manufacturer=manufacturer)
    elif manufacturer is None:
        result_kartridjes = Zapravka.objects.all()

    current_page = int(page_num)

    if view_w:
        view_w = True
        if result_kartridjes:

            paginator = Paginator(result_kartridjes, 8)
            try:
                result_kartridjes = paginator.page(page_num)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                result_kartridjes = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                result_kartridjes = paginator.page(paginator.num_pages)

    elif view_in:
        view_in = True
        result_kartridjes = Zapravka.objects.filter(manufacturer=manufacturer)

    context = {

        'result_kartridjes': result_kartridjes,
        'current_page': current_page,
        'manufacturer': manufacturer,
        # 'paginator': paginator,
        'view_w': view_w,
        'view_in': view_in,

    }


    return render(request, 'result_of_poisk_kart.html', context)

def zapravka(request):
    cart_id = request.GET.get("cart_id")


    query_1 = Zapravka.objects.all()

    poisk = cart_id
    poisk = int(poisk)

    if poisk:

        query_1 = Zapravka.objects.filter(

            Q(id=poisk)
        )

    for seo_con in query_1:
        short_n = seo_con.short_name
        long_n = seo_con.long_name
        manuf = seo_con.manufacturer
        price_v = seo_con.price_v

    return render(request, 'kartridj_detail.html', locals() )

def cartridges_of_printer(request):

    query = request.GET.get("dev_model")
    printeres = Zapravka.objects.filter(compatibility__name_dev=query)

    rem_printeres = Device.objects.filter(name_dev__iexact=query)


    context = {
        'rem_printeres':rem_printeres,
        'printeres':printeres,
        'query':query,

    }


    return render(request, 'cartridges_of_printer.html', context )

def searching(request):
    poisk = request.GET.get("poisk")
    view_w = request.GET.get("view_w")
    view_in = request.GET.get("view_in")

    if view_w:
        view_w = True
    elif view_in:
        view_in = True

    manufacturer = request.GET.get("manufacturer")
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1

    context = {}
    result_kartridjes = Zapravka.objects.all()

    if poisk:
        result_kartridjes= Zapravka.objects.filter(Q(long_name__icontains=poisk)|
                                                   # Q(manufacturer__icontains=poisk)|
                                                   Q(short_name__icontains=poisk)
                                                   # Q(compatibility__name_dev__icontains=poisk)

                                                   )



    paginator = Paginator(result_kartridjes, 8)
    try:
        result_kartridjes = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        result_kartridjes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        result_kartridjes = paginator.page(paginator.num_pages)
        
    if result_kartridjes:
        context = {

            'result_kartridjes': result_kartridjes,
            'poisk': poisk,
            'view_w': view_w,
            'view_in': view_in,
            'manufacturer': manufacturer,

        }

    else:
        sorry = 'Результат не найден'
        sorry2 = 'Если вы не нашли картридж через поисковую строку'
        sorry3 = 'Вы можете попробовать поискать его бренду'

        sorry4  = 'Также вы можете позвонить по телефону и уточнить о наличии заправки ваших картриджей у наших менеджеров'


        context = {'sorry': sorry, 'sorry2': sorry2, 'sorry3': sorry3, 'sorry4': sorry4, 'poisk': poisk, 'paginator': paginator}





    return render(request, 'result_of_poisk_kart_search.html', context)