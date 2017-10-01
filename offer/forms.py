from django import forms
from .models import Offer

class PostOffer(forms.ModelForm):
    
    class Meta:
        model = Offer
        fields = ('customerName', 'email', 'subject', 'message')