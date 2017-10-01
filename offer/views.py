from django.shortcuts import render

# Create your views here.
#A view is a place where we put the "logic" of our application

def show_offer_form(request):
    return render(request, 'offer/show_offer_form.html', {})