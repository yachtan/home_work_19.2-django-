from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        result = [item for item in cleaned_name.lower().split(' ') if item in self.banned_words]
        if result:
            raise forms.ValidationError('Использование недопустимых слов')
        else:
            return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        result = [item for item in cleaned_description.lower().split(' ') if item in self.banned_words]
        if result:
            raise forms.ValidationError('Использование недопустимых слов')
        else:
            return cleaned_description

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('category', )


class VersionForm(forms.ModelForm):

    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Version
        fields = '__all__'
