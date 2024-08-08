from django.shortcuts import render
from django.http import HttpResponse
from . import data
from .models import Product
from math import ceil

# Create your views here.

# # old view
# def index(request):
#     products = Product.objects.all()
#     n = len(products)
#     num_slides = n//4 + ceil((n/4)-(n//4))
#     # context = {"products":products, "num_slides":num_slides}
#     context = {"products":products, "range":range(1,num_slides), "num_slides":num_slides}
#     return render(request, "shop\index.html", context)
#     # return HttpResponse("shop index")

def index(request):
    allProds = []    
    catprods = Product.objects.values("category","product_id")
    cats = {items['category'] for items in catprods}
    print("🚀 ~ cat:", cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    
    context = {"allProds":allProds}
    return render(request, "shop\index.html", context)
    
def json_view(request):
    # data_ = data.states
    data_ = data.products
    context = {"data":data_}
    return render(request , "shop/json.html", context)
    return render(request , "shop/json.html")

def about(request):
    return HttpResponse("we are at about")

def contact(request):
    return HttpResponse("we are at contact")
    
def tracker(request):
    return HttpResponse("we are at tracker")
    
def search(request):
    return HttpResponse("we are at search")
    
def productview(request):
    return HttpResponse("we are at productview")
    
def checkout(request):
    return HttpResponse("we are at checkout")
    
