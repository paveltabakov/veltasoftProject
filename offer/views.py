from django.shortcuts import render
from .models import Offer #The dot(.) before models means current directory or current application
# Both views.py and models.py are in the same directory

# Create your views here.
#A view is a place where we put the "logic" of our application

def show_offer_form(request):
    offers = Offer.objects.all()
    return render(request, 'offer/show_offer_form.html', {'offers' : offers})
    