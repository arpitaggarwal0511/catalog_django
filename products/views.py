from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Products
from django.db.models import Q

def product_list(request):
    qs = Products.objects.all().order_by('-id')

    # text search
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

    # size exact match
    size = request.GET.get('size', '').strip()
    if size:
        qs = qs.filter(size=size)

    # price filters
    min_price = request.GET.get('min_price', '').strip()
    if min_price:
        try:
            min_price_val = float(min_price)
            qs = qs.filter(price__gte=min_price_val)
        except ValueError:
            pass

    max_price = request.GET.get('max_price', '').strip()
    if max_price:
        try:
            max_price_val = float(max_price)
            qs = qs.filter(price__lte=max_price_val)
        except ValueError:
            pass

    # rating filter
    min_rating = request.GET.get('min_rating', '').strip()
    if min_rating:
        try:
            min_rating_val = float(min_rating)
            qs = qs.filter(rating__gte=min_rating_val)
        except ValueError:
            pass

    return render(request, "products/product_list.html", {"products": qs, "request": request})

def product_detail_json(request, pk):
    p = get_object_or_404(Products, pk=pk)
    data = {
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": str(p.price),
        "rating": p.rating,
        "size": p.size,
        "image_url": p.image_url,
    }
    return JsonResponse(data)
