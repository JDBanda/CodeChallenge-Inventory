from django.urls import path

from api.views import ProductsView

urlpatterns = [
    path('<int:pk>', ProductsView.as_view(), name='product_ids'),
    path('', ProductsView.as_view(), name='products_methods'),
]
