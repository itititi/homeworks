from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from models import Phone

def catalog(request):
    phones = Phone()
    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    return render(request, 'catalog.html', {'phones': phones})

def phone_details(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_details.html', {'phones': phone})
