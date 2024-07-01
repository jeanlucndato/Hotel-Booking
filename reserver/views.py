from django.shortcuts import render, get_object_or_404
from .reserver import Reserver
from serena_app.models import Product
from django.http import JsonResponse

# Create your views here.


def reserver_summary(request):
    #get the cart
    reserver = Reserver(request)
    reserver_products = reserver.get_prods
    return render(request, "reserver_summary.html", {"reserver_products":reserver_products})

def reserver_add(request):
    
    reserver = Reserver(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        reserver.add(product=product)
        #get cart quqntity
        cart_quantity = reserver.__len__()
        
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response
    
    

def reserver_delete(request):
    pass

def reserver_update(request):
    pass