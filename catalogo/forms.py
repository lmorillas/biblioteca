from django.forms import ModelForm, DateInput
from catalogo.models import Author
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class AuthorForm(ModelForm):
    '''Formulario para crear autores'''
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'date_of_death': DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('date_of_birth', css_class='form-group col-md-6 mb-0'),
                Column('date_of_death', css_class='form-group col-md-6 mb-0'),
                css_class='form-row my-2'
            ),
            Submit('submit', 'Enviar')
        )

