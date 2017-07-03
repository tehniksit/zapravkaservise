from django import forms
from main.kartridji_zapravka.models import *


class ZapravkaForm(forms.ModelForm):

    class Meta:

        model = Zapravka

        exclude = [""]




