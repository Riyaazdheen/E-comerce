from django.shortcuts import render, redirect
from Account.models import UserModel
from Home.models import Products

# Create your views here.
def carthome(request):
    if request.user.is_authenticated:
        prods = UserModel.objects.get(user=request.user).prod.all()
        return render(request, 'Cart/Cart.html', {'prods':prods})
    else:
        return render(request, 'Cart/cart_sign_in.html')

def addtocart(request, id):
    prod = Products.objects.get(id=id)
    usermodel = UserModel.objects.get(user=request.user)
    usermodel.prod.add(prod)
    return redirect('home:home')

def removefromcart(request, id):
    prod = Products.objects.get(id=id)
    usermodel = UserModel.objects.get(user=request.user)
    usermodel.prod.remove(prod)
    return redirect('cart:carthome')