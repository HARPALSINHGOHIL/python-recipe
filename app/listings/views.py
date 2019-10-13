from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing
from .choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    context = {'listings': paginator.get_page(page)}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    context = {
        'listing': get_object_or_404(Listing, pk=listing_id)
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    keywords = request.GET.get('keywords')
    if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    city = request.GET.get('city')
    if city:
        queryset_list = queryset_list.filter(city__iexact=city)

    # State
    state = request.GET.get('state')
    if state:
        queryset_list = queryset_list.filter(state__iexact=state)

    # Bedroom
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    price = request.GET.get('price')
    if price:
        queryset_list = queryset_list.filter(price__lte=price)
        
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
