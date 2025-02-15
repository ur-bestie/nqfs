from django import forms
from .models import KYCInfo

class KYCForm(forms.ModelForm):
    class Meta:
        model = KYCInfo
        fields = ['full_name', 'email', 'ssn', 'passport', 'drivers_license']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
            }),
            'ssn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '123-45-6789',
                'pattern': r'\d{3}-\d{2}-\d{4}',
                'title': 'Format: 123-45-6789',
            }),
            'passport': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf, .jpg, .png',
            }),
            'drivers_license': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf, .jpg, .png',
            }),
        }
