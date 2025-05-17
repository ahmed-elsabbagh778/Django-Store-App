from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product description',
                'rows': 3,
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'creation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'expiry_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter user name',
            'autofocus': 'autofocus',
        }))
    email = forms.EmailField(
         widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password',
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password',
        })
    )