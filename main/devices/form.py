from django import forms
from main.devices.models import *


class PriceForm(forms.ModelForm):

    class Meta:

        model = Device
        exclude = [""]

class TypeOfWorkForm(forms.ModelForm):

    class Meta:

        model = TypeOfWork
        exclude = [""]

class DeviceCategoryForm(forms.ModelForm):

    class Meta:

        model = DeviceCategory
        exclude = [""]

class RelationsForm(forms.ModelForm):

    class Meta:

        model = Relations
        exclude = ["image_printer"]




