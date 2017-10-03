from django import forms
from .models import Offer
from django.utils.translation import gettext_lazy as _

class PostOfferForm(forms.ModelForm):
    
    customerName = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField(label=_("Email address"))
    message = forms.CharField()
    
    class Meta:
        model = Offer
        fields = ('customerName', 'email', 'subject', 'message')
