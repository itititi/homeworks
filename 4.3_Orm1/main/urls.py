from django.urls import path
from phones.views import catalog, phone_details

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('catalog/<slug:slug>/', phone_details, name='phone_details'),
]
