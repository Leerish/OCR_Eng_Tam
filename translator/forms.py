# translator/forms.py

from django import forms
from .models import TranslationRequest

class TranslationRequestForm(forms.ModelForm):
    class Meta:
        model = TranslationRequest
        fields = ['newspaper_name', 'edition', 'image']
