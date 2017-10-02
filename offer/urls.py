from django.conf.urls import url
from . import views # import all views from offer APP


urlpatterns = [
    url(r'^$', views.show_offer_form, name='show_offer_form'),
    url(r'save/', views.send, name='save'),
]