from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.


def home(request):
    return render(request, "store/index.html")


def collections(request):
    category = Category.objects.filter(status=0)
    context = {"category": category}
    return render(request, "store/collections.html", context)


def collectionsviews(request, slug):
    if Category.objects.filter(slug=slug, status=0):
        product = Product.objects.filter(category__slug=slug)
        print(product)
        category = Category.objects.filter(slug=slug).first()
        context = {"products": product, "category": category}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "not such category")
        return redirect("collections")


def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            product = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {"product": product}
        else:
            messages.error(request, "No such Product found")
            return redirect("collections")
    else:
        messages.error(request, "No such category found")
        return redirect("collections")
    return render(request, "store/products/view.html", context)