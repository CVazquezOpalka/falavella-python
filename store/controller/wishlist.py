from store.models import Product, WishList
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="login")
def index(request):
    whislist_items = WishList.objects.filter(user=request.user)
    context = {"wishlist": whislist_items}
    return render(request, "store/wishlist.html", context)


def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if WishList.objects.filter(user=request.user, product_id=prod_id):
                    return JsonResponse(
                        {"status": "The product has been enter in the wishlist"}
                    )
                else:
                    WishList.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse(
                        {"status": "Product added to wishlist succesfully"}
                    )

            else:
                return JsonResponse({"status": "No such Productfound"})
        else:
            return JsonResponse({"status": "Login to Continue"})
    return redirect("home")


def delete_to_wishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            print(prod_id)
            if WishList.objects.filter(user=request.user, product_id=prod_id):
                item = WishList.objects.get(user=request.user, product_id=prod_id)
                item.delete()
                return JsonResponse(
                    {"status": "Product has been removed from wishlist"}
                )
            else:
                return JsonResponse({"status": "Product do not match in the wishlist"})
        else:
            return JsonResponse({"status": "Login to continue"})
    return redirect("home")
