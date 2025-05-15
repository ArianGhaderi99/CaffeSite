from django import forms
from pages.models import Order, Contact

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'Addres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your delivery address',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'pattern': '[0-9]{10,12}',
                'title': 'Please enter a valid phone number',
                'required': True
            }),
            'coffee_type': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }, choices=[
                ('', 'Select your coffee'),
                ('espresso', 'Espresso'),
                ('americano', 'Americano'),
                ('latte', 'Latte'),
                ('cappuccino', 'Cappuccino'),
                ('mocha', 'Mocha'),
            ]),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter weight in grams',
                'min': '50',
                'max': '1000',
                'required': True
            })
        }

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your message',
        'rows': 5,
        'required': True
    }))

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'pattern': '[0-9]{10,12}',
                'title': 'Please enter a valid phone number',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'required': True
            })
        }
