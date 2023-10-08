from django.shortcuts import render,HttpResponse
from .models import ProductDetail


# Create your views here.
def product(request):
    products=ProductDetail.objects.all()
    context={
        'products':products
    }
    return render(request,'products.html',context)

def product_payment(request,id):
    pro=ProductDetail.objects.get(id=id)
    
    con={
        'product':pro
    }
    return render(request,"esewa.html",con)

def home(request):
    
    return render(request,"home.html")

