from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def product_list(request):
    qs = Products.objects.all().order_by('-id')
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
    size = request.GET.get('size', '').strip()
    if size:
        qs = qs.filter(size=size)    
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