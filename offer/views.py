from django.shortcuts import render
from .models import Offer  # The dot(.) before models means current directory or current application
# Both views.py and models.py are in the same directory
from .forms import PostOfferForm
from django.contrib import messages
# Create your views here.
# A view is a place where we put the "logic" of our application

def show_offer_form(request):
    offers = Offer.objects.all()
    return render(request, 'offer/show_offer_form.html', {'offers' : offers})


def send(request):
    if request.method == "POST":
        # Get posted form
        offerForm = PostOfferForm(request.POST)  # If method is POST then we want to construct the PostOfferForm with data from the form!
        if offerForm.is_valid():
            #email = offerForm.cleaned_data['email']
            offerForm.save()
            successText = "Your request is send! Thank you!"
            messages.success(request, successText)
            return render(request, 'offer/show_offer_form.html')
        else:
            errorText = "Form is not valid!!!"
            messages.error(request, errorText)
            return render(request, 'offer/show_offer_form.html') 
    else:
        offerForm = PostOfferForm()
    return render(request, 'offer/show_offer_form.html', {'offerForm':offerForm})
            
    
