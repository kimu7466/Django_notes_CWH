from django.urls import path
from .views import index, about, contact, tracker, search, productview, checkout, json_view

urlpatterns = [
    path("", index, name="ShopHome"),
    path("about/", about, name="AboutUs"),
    path("contact/", contact, name="ContactUs"),
    path("tracker/", tracker, name="TrackingStatus"),
    path("search/", search, name="Search"),
    path("productview/", productview, name="ProductView"),
    path("checkout/", checkout, name="Checkout"),    
    
    path("json_view/", json_view, name="json_view"),
]
