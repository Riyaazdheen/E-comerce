from django.urls import path
from .views import carthome, addtocart, removefromcart
app_name = 'cart'

urlpatterns = [
    path('', carthome, name='carthome'),
    path('add/<id>', addtocart, name='addtocart'),
    path('remove/<id>', removefromcart, name='removefromcart'),
]
