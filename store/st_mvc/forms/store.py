from django import forms
from django.core.exceptions import ValidationError
from ..models import Category, Store

# Auxiliar
from ..auxiliar.constants import NAME_MIN_LENGTH, NAME_MAX_LENGTH
from ..auxiliar.validators import validate_length

# Crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field as F, HTML, Row, Column
from crispy_bootstrap5.bootstrap5 import Field, FloatingField


class StoreForm(forms.ModelForm):
    # Datos a mostrar con componentes en específico
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple,
    )

    dir = forms.CharField(
        label="Dirección",
        widget=forms.TextInput,
        help_text='Introduzca la direccion de la tienda',
        error_messages={'required': 'Debe introducir una direccion'}
    )

    name = forms.CharField(
        label="Nombre",
        help_text="Introduzca el nombre de la tienda",
        widget=forms.TextInput(attrs={
            'placeholder': "7 eleven",
            'max': 7,
            'min': 3
        }),
        error_messages={
            'required': 'Debe introducir el nombre'
        }
    )

    # Info del formulario
    class Meta:
        model = Store  # Modelo a utilizar en el formulario
        fields = ('name', 'dir', 'category')  # Campos a mostrar, Ojo el orden importa

    # Init es el constructor de las clases
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionamos la ayuda de cripsy para crear el layout
        self.helper = FormHelper()
        # Create Layout
        self.helper.layout = Layout(
            Row(
                Column(FloatingField('name')),
                Column(FloatingField('dir')),
            ),

            Field('category'),
            Column(
                Submit("create_store", "Crear tienda", css_class='btn-success button-form'),  # id. Nombre.
                HTML('<a href="{% url "st_mvc:index" %}" class="btn btn-danger button-form"> Cancelar </a> '),
                css_class='button-form'
            )

        )

    # Estos validadores salen al principio del formulario
    # Este método va primero que el de form valid en el view
    def clean(self):
        print("here 2")
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        dir = cleaned_data.get('dir')
        validate_length('nombre', NAME_MAX_LENGTH, NAME_MIN_LENGTH)(name)
        validate_length('direccion', NAME_MAX_LENGTH, NAME_MIN_LENGTH)(dir)



