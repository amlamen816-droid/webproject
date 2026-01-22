from django import forms
from .models import MercedesCar

class MercedesCarForm(forms.ModelForm):
    class Meta:
        model = MercedesCar
        fields = [
            'name',
            'model_year',
            'price',
            'image',
            'description'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Car Name'
            }),

            'model_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Model Year'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
                'placeholder': 'Price'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Car Description'
            }),
        }
