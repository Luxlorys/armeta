from typing import ChainMap
from django.shortcuts import render, redirect
from .models import *
from django.db.models import F


dic = {}
all_object = []


def index(request):
    return render(request, 'main/index.html')

    
def catalog(request):
    products = Product_details.objects.order_by('-product_price')
    return render(request, 'main/catalog.html', {
        'products': products
    }) 

    
def complete(request):
    complete_pc = Complete_PC.objects.order_by('-price')
    return render(request, 'main/complete.html', {
        'complete_pc': complete_pc
    }) 


def cart(request, id):
    user = request.user
    product = Product_details.objects.get(id = int(id))
    print(request.session.keys())
    st = []
    product_in_cart = add_to_cart.objects.filter(id = int(id))

    if not product_in_cart:
        insert_in_table = add_to_cart(id = int(id), username = user, product_name = product.product_name, quantity=1)
        insert_in_table.save()

    else:
        add_to_cart.objects.filter(id = int(id)).update(quantity=F('quantity') + 1)

    return redirect('show_cart')


def show_cart(request):
    b = add_to_cart.objects.filter(username = request.user)
    a = []
    total_price = 0
    for i in b:
            a.append(i)
    d = []
    
    for i in a:
        product = Product_details.objects.get(id=i.id)
        d.append(product)
        product_price = product.product_price
        total_price = total_price + product_price

    return render(request, 'main/cart.html', {'data': zip(d, a), 'total_price': int(total_price)})


def checkout(request):
    return render(request, 'main/checkout.html')


def success(request):
    return render(request,'main/success.html')