from django.shortcuts import render
from .models import Products
from .models import crosel  
from Account.models import UserModel

# Create your views here.
def home(request):
    context = {
        'products':Products.objects.all(),
        'corsels':crosel.objects.all()
    }
    if request.user.is_authenticated:
        usermodel = UserModel.objects.get(user=request.user)
        cart_count = len(usermodel.prod.all())
        context['cart_count'] = cart_count
    return render(request, "Home/index.html", context)
    

