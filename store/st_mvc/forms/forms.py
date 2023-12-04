from django import forms
from ..auxiliar.constants import length_error, START_UPPER_CASE
from ..auxiliar.validators import validate_first_letter_uppercase
from ..models import VideoGames, Category

# Cripsy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field as F, HTML, Row, Column


class ParamForm(forms.Form):
    title = forms.CharField(
        error_messages={'max_length': length_error(field='Título', length='5', max=True)},
        min_length=1,
        max_length=5,
        help_text='Introduzca el título',
        label='Título',
        required=True)
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
        help_text='Introduza el mensaje',
        label='Mensaje',
        error_messages={'upper_case': START_UPPER_CASE},
        validators=[validate_first_letter_uppercase], )

    def is_valid(self):
        print("El formulario es valido")
        return super().is_valid()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        print(title)
        print("Clean Data")


class VideoGamesForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        widget=forms.Select(),
        help_text='Seleccione una categoría',
        error_messages={'required': 'Debe seleccionar una categoría'},
        required=True,
        label='Categorías',
        queryset=Category.objects.all()
    )

    class Meta:
        model = VideoGames  # Modelo a utilizar en el formulario
        fields = ('image', 'description', 'rate', 'category')  # Campos a mostrar, Ojo el orden importa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionamos la ayuda de cripsy para crear el layout
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Row(
                Column(F('image')),
                Column(F('rate')),
                Column(F('category'))
            ),
            Row(
                Column(F('description'))
            ),
                Column(
                    Submit("create_store", "Enviar", css_class='btn-success button-form'),  # id. Nombre.
                    HTML('<a href="{% url "st_mvc:forms" %}" class="btn btn-danger button-form"> Cancelar </a> '),
                    css_class='button-form'
            ))


