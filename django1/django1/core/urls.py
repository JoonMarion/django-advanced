from django.urls import path, include
from .views import home, contact, product

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>/', product, name='product'),
]
