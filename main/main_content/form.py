from django import forms
from main.main_content.models import *


class MainPageForm(forms.ModelForm):

    class Meta:

        model = MainPage
        exclude = [""]

class TextRajonyForm(forms.ModelForm):

    class Meta:

        model = TextRajony
        exclude = [""]



