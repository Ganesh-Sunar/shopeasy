from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Product

# Create your views here.
def preview_404(request):
    return render(request,'404.html')


def home(request):
    return render(request,'shop/home.html')

def about(request):
    context = {
            'company_name': 'ShopEasy Pvt. Ltd.',
            'founded_year': 2026,
            'about_text': "ShopEasy started in 2026 with a simple idea — online shopping should be "
                          "easy, fast, and reliable, especially for people right here in Nepal. What "
                          "began as a small project has grown into a platform offering everything from "
                          "electronics and fashion to home essentials and books, all in one place. We "
                          "work directly with trusted suppliers to make sure every product meets our "
                          "quality standards before it reaches your doorstep. Our goal is simple: "
                          "make online shopping something you can actually trust.",
            'team_members': [
                {'name': 'Amrit Sunar', 'role': 'Founder & CEO'},
                {'name': 'Leo Wazi', 'role': 'Lead Developer'},
                {'name': 'Shankar Sunar', 'role': 'Product Manager'},
            ],
        }
    return render(request,'shop/about.html',context)

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