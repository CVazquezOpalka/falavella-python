from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Cart, Order, OrderItems, Product, Profile
from django.contrib.auth.models import User


@login_required(login_url="login")
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty
        
    userprofile = Profile.objects.filter(user=request.user).first()    
    context = {"cartitems": cartitems, "total_price": total_price, "profile":userprofile}
    return render(request, "store/checkout.html", context)


@login_required(login_url="login")
def placeorder(request):
    if request.method == "POST":
        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get("fname")
            currentuser.last_name = request.POST.get("lname")
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get("phone")
            userprofile.address = request.POST.get("address")
            userprofile.city = request.POST.get("city")
            userprofile.state = request.POST.get("state")
            userprofile.country = request.POST.get("country")
            userprofile.zipcode = request.POST.get("zipcode")
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get("fname")
        neworder.lname = request.POST.get("lname")
        neworder.email = request.POST.get("email")
        neworder.phone = request.POST.get("phone")
        neworder.address = request.POST.get("address")
        neworder.city = request.POST.get("city")
        neworder.state = request.POST.get("state")
        neworder.country = request.POST.get("country")
        neworder.zipcode = request.POST.get("zipcode")
        neworder.fname = request.POST.get("fname")
        neworder.payment_mode = request.POST.get("payment_mode")

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = (
                cart_total_price + item.product.selling_price * item.product_qty
            )

        neworder.total_price = cart_total_price
        trackno = f"{request.user}" + str(random.randint(1111111, 9999999))
        while Order.objects.filter(traking_no=trackno) is None:
            trackno = f"{request.user}" + str(random.randint(1111111, 9999999))

        neworder.traking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItems.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty,
            )

            # to decrece Product into stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        # Clear user cart
        Cart.objects.filter(user=request.user).delete()

        messages.success(request, "Your order has been paced successfully")

    return redirect("home")