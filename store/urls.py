from django.urls import path
from . import views
from store.controller import authview, cart, wishlist


urlpatterns = [
    path("", views.home, name="home"),
    path("collections/", views.collections, name="collections"),
    path("collections/<str:slug>", views.collectionsviews, name="collectionsview"),
    path(
        "collections/<str:cate_slug>/<str:prod_slug>",
        views.productview,
        name="productview",
    ),
    path("register/", authview.register, name="register"),
    path("login/", authview.loginpage, name="login"),
    path("logout/", authview.signout, name="logout"),
    path("add-to-cart", cart.add_to_cart, name="addtocart"),
    path("cart/", cart.viewcart, name="cart"),
    path("update-cart", cart.update_cart, name="updatecart"),
    path("delete-cart-item", cart.delete_item, name="deletecartitem"),
    path("wishlist", wishlist.index, name="wishlist"),
    path("add-to-wishlist", wishlist.addtowishlist, name="addtowishlist"),
    path("delete-to-wishlist", wishlist.delete_to_wishlist,name="deletetowishlist")
]
