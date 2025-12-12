from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:pk>/json/", views.product_detail_json, name="product_detail_json"),

]
