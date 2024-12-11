from django.shortcuts import render

from catalog.models import Product

def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'base.html', context)
