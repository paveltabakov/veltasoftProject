from django import forms
from .models import Offer

class PostOfferForm(forms.ModelForm):
    
    class Meta:
        model = Offer
        fields = ('customerName', 'email', 'subject', 'message')