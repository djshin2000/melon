from django.forms import ModelForm
from django import forms

from .models import Artist

__all__ = (
    'ArtistAddForm',
)


class ArtistAddForm(ModelForm):
    class Meta:
        model = Artist
        fields = [
            'img_profile',
            'name',
            'real_name',
            'nationality',
            'birth_date',
            'constellation',
            'blood_type',
            'intro',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
