from django import forms
from .models import Orders

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"

        labels = {
            'oid': 'Order ID',
            'fname': 'First Name',
            'lname': 'Last Name',
            'price': 'Price',
            'mail': 'Email ID',
            'addr': 'Address',
        }

        widgets = {
            'oid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 101'}),
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. John'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Doe'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 100'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. abc@xyz.com'}),
            'addr': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g. IN'}),
        }