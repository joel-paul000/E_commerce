from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from UserApp.models import*


def hey(request):
    return render(request,"hey.html")

def index(request):
    return render(request,"index1.html")

def cateogory(request):
                if request.method == "POST":
                    cateogoryname  = request.POST ['catname']
                    Category.objects.create(
                        cateogoryname =  cateogoryname,
                    )
                return render (request,'cateogory.html')    


def product(request):
    categories = Category.objects.all()
    context = {
          'categories':categories
    }
    if request.method == "POST":
             productname = request.POST ['productname']
             productquantity = request.POST ['productquantity']
             productimage =request.FILES ['productimage']
             productprice=request.POST ['productprice']
             cateogoryname=request.POST ['cateogoryname']

             Product.objects.create(
                productname = productname,
                productquantity=productquantity,
                productimage=productimage,
                productprice=productprice,
                category_id=Category.objects.get(id=cateogoryname)
             )


    return render(request,"product.html", context)


def viewcat(request):
      
    details = Category.objects.all()
    context = {
        'details':details
    }
    return render(request,'viewcat.html',context)

def viewpro(request):
      details= Product.objects.all()
      context={
            'details':details
      }
      return render(request,'viewpro.html',context)

def delete(request,sample_id):
    Category.objects.filter(id=sample_id).delete()
    return redirect('viewcat')

def deletepro(request,sample_id):
    Product.objects.filter(id=sample_id).delete()
    return redirect('viewpro')

def updatecateogory(request,sample_id):
    details=Category.objects.filter(id=sample_id)
    context ={
        'details':details,
    }

    return render(request,'updatecateogory.html',context)

def store(request,sample_id):
    if request.method == "POST":
                    cateogoryname  = request.POST ['catname']
                    Category.objects.filter(id=sample_id).update(
                        cateogoryname =  cateogoryname,)
                    return redirect('viewcat')
    return render(request,'updatecateogory.html')

def updateproduct(request,sample_id):
      details=Product.objects.filter(id=sample_id)
      context ={
        'details':details,
      }
      return render(request,'updateproduct.html',context)

def productstore(request,sample_id):
    if request.method == "POST":
        productname = request.POST ['productname']
        productquantity = request.POST ['productquantity']
        productimage =request.FILES ['productimage']
        productprice=request.POST ['productprice']
        cateogoryname=request.POST ['cateogoryname']
        Product.objects.filter(id=sample_id).update(
                productname = productname,
                productquantity=productquantity,
                productimage=productimage,
                productprice=productprice,
                category_id=Category.objects.get(id=cateogoryname))
        return redirect('viewpro')
    return render(request,'updateproduct.html')


def viewcustomer(request):
      details=Register.objects.all()
      context={
            'details':details
      }
      return render(request,'viewcustomer.html',context)


def deletecus(request,sample_id):
   Register.objects.filter(id=sample_id).delete()
   return redirect('viewcustomer')


def vieworder(request):
      data = checkout.objects.all()
      context={
            'data':data
      }
      return render(request,"vieworder.html",context)
def deleteorder(request,sample_id):
    checkout.objects.filter(id=sample_id).delete()
    return redirect('vieworder')

def logoutadmin(request):
    request.session.flush()
    return redirect('login')




# Create your views here.
