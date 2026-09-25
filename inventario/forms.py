from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:

        model = Producto

        fields = [
            'nombre',
            'precio',
            'stock',
            'categoria',
            'imagen'
        ]

        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),

            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio',
                    'step': '0.01'
                }
            ),

            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el stock'
                }
            ),

            'categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la categoría'
                }
            ),

            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://ejemplo.com/imagen.jpg'
                }
            ),
        }