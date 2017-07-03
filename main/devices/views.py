from django.db.models import Q
from django.shortcuts import render
from main.devices.form import *



def brand_choose(request):


    return render(request, 'brand_choose.html', locals() )

def device(request):
    brand = request.GET.get("brand")

    form_class = RelationsForm(Relations)

    form = RelationsForm(instance=Relations())
    if brand:
        form.fields["dev_model"].queryset = Device.objects.filter(name_dev__icontains=brand)


    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'




    return render(request, 'printer_choose.html', locals(), {'form': form, })


def detail_of_printer(request):

    query = request.GET.get("dev_model")
    if query:

        query_1 = Relations.objects.all()
        query_1 = query_1.filter(

            Q(dev_model__id__icontains=query)
        )
        for pic in query_1:
            pic_path = str(pic.image_printer)


    form_class = RelationsForm(Relations)
    if request.method == "POST":
        form = RelationsForm(request.POST, instance=Relations())

    else:
        form = RelationsForm(instance=Relations())

    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'


        return render(request, 'choosing_print.html', locals(), {'form': form, })





