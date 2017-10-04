import json
import urllib

from django.shortcuts import render
from .models import Offer  # The dot(.) before models means current directory or current application
# Both views.py and models.py are in the same directory
from .forms import PostOfferForm
from django.contrib import messages
# Create your views here.
# A view is a place where we put the "logic" of our application
from django.conf import settings

def show_offer_form(request):
    offers = Offer.objects.all()
    return render(request, 'offer/show_offer_form.html', {'offers' : offers})


def send(request):
    if request.method == "POST":
        # Get posted form
        offerForm = PostOfferForm(request.POST)  # If method is POST then we want to construct the PostOfferForm with data from the form!
        if offerForm.is_valid():
           #''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            #''' End reCAPTCHA validation '''
            if result['success']:
                offerForm.save()
                messages.success(request, "Your request is send! Thank you!")
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        else:
            messages.error(request, "Form is not valid!!!")
            return render(request, 'offer/show_offer_form.html') 
    else:
        offerForm = PostOfferForm()
    return render(request, 'offer/show_offer_form.html', {'offerForm':offerForm})
            
    
