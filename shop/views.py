from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Product

# Create your views here.
def preview_404(request):
    return render(request,'404.html')


def home(request):
    return render(request,'shop/home.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if name and email and message:
          messages.success(request,f"Thanks! {name} message recieved!")
    context={
       'Address':'Gorkha Nepal',
       'Email': 'shopeasy@gmail.com',
    }
    return render(request,"shop/contact.html",context)

def product_list(request):
    products = Product.objects.all()
    context={
        'products':products,
        'product_count':products.count(),
    }
    return render(request,'shop/product_list.html',context)

def product_details(request,pk):
    product = get_object_or_404(Product,pk=pk)
    context = {
        "product":product
    }
    return render(request,"shop/product_details.html")