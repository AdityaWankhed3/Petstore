from math import ceil
from django.shortcuts import render, redirect, HttpResponse
from petapp.models import contacts2
from django.contrib import messages
from petapp.models import product


# Create your views here.

def home(request):
    return render(request,'petapp/home.html')
def base(request):
    return render(request,'petapp/base.html')
def about(request):
    return render(request,'petapp/about.html')
def services(request):
    return render(request,'petapp/services.html')
def copy(request):
    return render(request,'petapp/copy.html')
def contact1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phone = request.POST.get('phone')
        
        myquery = contacts2(name=name, email=email, desc=desc, phone=phone)
        myquery.save()
        messages.info(request,'Will get back to you soon....')
    return render(request,'petapp/contact.html')


def home(request):
    allProds=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params= {"allProds": allProds}
    return render(request,"petapp/home.html", params)

def checkout(request):
    return render(request,'petapp/checkout.html')