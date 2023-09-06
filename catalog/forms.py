from django import forms

from catalog.models import Product, Version


class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'sing_current_version':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in words:
            if i in cleaned_data:
                raise forms.ValidationError('Вы используете запрещённые слова')

        return cleaned_data


class VersionForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
