from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    # Next line overrides title attr of the product
    title = forms.CharField(
        label='Product title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Any title'
            }
        )
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    # Default required is True
    title = forms.CharField(
        label='Product title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Any title'
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'my_id',
                'class': 'new-class-name two',
                'placeholder': 'Any description'
                'rows': 20,
                'columns': 120
            }
        )
    )
    price = forms.DecimalField(initial='0.00')
