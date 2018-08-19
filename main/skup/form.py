# -*- coding: utf-8 -*-
from django import forms
from main.skup.models import *


class SkupFormHP(forms.ModelForm):

    class Meta:

        model = HP
        exclude = [""]

class SkupFormBrother(forms.ModelForm):

    class Meta:

        model = Brother
        exclude = [""]

class SkupFormKyocera(forms.ModelForm):

    class Meta:

        model = Kyocera
        exclude = [""]

class SkupFormCanon(forms.ModelForm):

    class Meta:

        model = Canon
        exclude = [""]



class SkupFormSamsung(forms.ModelForm):

    class Meta:

        model = Samsung
        exclude = [""]










