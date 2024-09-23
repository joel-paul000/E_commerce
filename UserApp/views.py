from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from AdminApp.models import *
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import *
from .models import Cart, Register, Product

#

def home(request):
    return render(request,"hello.html")


def ind(request,):
 
 user_name = request.session.get('u_name')
 details= Product.objects.all()
 context={
            'details':details,
            'user_name':user_name

      }
 return render(request,'userindex.html',context)

def login(request):
     if request.method == "POST":
          username = request.POST ['username']
          password = request.POST ['password']

          if Register.objects.filter(username = username, password=password).exists():
               data = Register.objects.filter(username = username, password=password).values('username', 'id').first()
               request.session['u_id'] = data['id']
               request.session['u_name'] = data['username']
               return redirect('ind')
          
          else:
               return redirect('login')
     return render(request,'login.html')
 
def regist(request):
    if request.method == "POST":
             username = request.POST ['username']
             phonenumber = request.POST ['phonenumber']
             email = request.POST['email']
             password =request.POST ['Password']

             Register.objects.create(
                  username = username,
                  phonenumber = phonenumber,
                  email=email,
                  password = password)
             
    return render(request,'register.html')


def cat(request):
     details= Product.objects.all()
     deta=Category.objects.all
     context={
          "details":details,
          "deta":deta}
     return render(request,'usercateogory.html',context)


def cart(request,sample_id):
     user_id_id=request.session.get("u_id")
     # if Cart.objects.filter(user_id_id=user_id_id,product_id=sample_id).exists():
     #      return redirect('ind')
     #productquantity=request.session.get('productquantity')
     if Cart.objects.filter(user_id=user_id_id,product_id=sample_id).exists():

          quantity =  Cart.objects.get(product_id=sample_id,user_id_id=user_id_id)
          quantity.productquantity += 1
          quantity.save()
     else:
          Cart.objects.create(
          user_id_id=user_id_id,
          product_id=Product.objects.get(id=sample_id),
          totalamount = Product.objects.get(id=sample_id).productprice,
     )
     return redirect('viewcart')



def viewcart (request):
     user_id=request.session.get('u_id')
     details=Cart.objects.filter(user_id=user_id)
     context = {
         'details':details,
          }
     return render(request,'cart.html',context)
def checkouttt(request):
   user_id=request.session.get('u_id')
   details=Cart.objects.filter(user_id=user_id)
   context= {
         'details':details,
          } 
   return render(request,'checkout.html',context)

def checkoutpro(request):
     if request.method == "POST":
                user_id_id=request.session.get("u_id")
                address = request.POST ['address']
                country = request.POST ['country']
                state = request.POST ['city']
                pincode = request.POST ['pincode']
                details= Cart.objects.filter(user_id=user_id_id)
                for i in details:
                     checkout.objects.create(
                          user_id=Register.objects.get(id=user_id_id),
                          product_id=Product.objects.get(id=i.product_id.id),
                          address=address,
                          country=country,
                          city=state,
                          pincode=pincode,)
     return redirect('checkoutt')

#def check(request):
   #user_id_id=request.session.get("u_id")
   #details= Cart.objects.filter(user_id = user_id_id)
   #return render(request,'checkout.html',{'details':details})


def confirmation(request):
     user_id=request.session.get('u_id')
     details=Cart.objects.filter(user_id=user_id)
     context= {
         'details':details,
          } 
     return render(request,'conformation.html',context)

def viewmore(request,sample_id):
    details=Product.objects.filter(id=sample_id)
    context={
            'details':details
          
      }
    return render(request,'viewmore.html',context)


def store(request,sample_id):
    if request.method == "POST":
         productname = request.POST ['productname']
         productquantity = request.POST ['productquantity']
         productimage =request.FILES ['productimage']
         productprice=request.POST ['productprice']
         cateogoryname=request.POST ['cateogoryname']
         Cart.objects.filter(id=sample_id).create(
           productname = productname,
                productquantity=productquantity,
                productimage=productimage,
                productprice=productprice,
                category_id=Category.objects.get(id=cateogoryname)
        )
         return redirect('ind')
    return render(request,'cart.html')


def deletecart(request,sample_id):
    Cart.objects.filter(id=sample_id).delete()
    return redirect('viewcart')


def catt(request):
     return render(request,'cart.html')

def viewcateogories(request,id):
    product = Product.objects.filter(id = id)
    context={
         'prodcut':product
    }
    return render(request,"viewcateogories.html",context)

def logout(request):
    request.session.flush()
    return redirect('login')

def buyedproducts(request,sample_id):
      user_id_id=request.session.get("u_id")
      checkout.objects.create(
          user_id_id=user_id_id,
          product_id=Cart.objects.get(id=sample_id),
         
     )
      return redirect("viewbuyed")


def viewbuyed (request):
     user_id=request.session.get('u_id')
     details=checkout.objects.filter(user_id=user_id)
     context = {
         'details':details,
          }
     return render(request,'buyedproduct.html',context)

def buyed(request,sample_id):
    if request.method == "POST":
         productname = request.POST ['productname']
         productquantity = request.POST ['productquantity']
         productimage =request.FILES ['productimage']
         productprice=request.POST ['productprice']
         cateogoryname=request.POST ['cateogoryname']
         checkout.objects.filter(id=sample_id).create(
           productname = productname,
                productquantity=productquantity,
                productimage=productimage,
                productprice=productprice,
                category_id=Category.objects.get(id=cateogoryname)
        )
         return redirect('checkout')
    return render(request,'buyedproduct.html')

def userprofile(request):
    user_id = request.session.get('u_id')
    data = Register.objects.get(id = user_id)
    return render(request,'userprofile.html',{'data':data})


def editprofile(request):
    user_id = request.session.get('u_id')
    data = Register.objects.get(id = user_id)
    context={
         'data':data
    }
    return render(request,'editprofile.html',context)
def updateprofile(request):
        if request.method == "POST":
            user_id = request.session.get('user_id')
            username = request.POST('username')
            email = request.POST('email')
            phonenumber = request.POST('phonenumber')
            Register.objects.filter(id = user_id).update(
                 username = username,
                 email = email,
                 phonenumber = phonenumber)
            return redirect('userprofile')
        


#def checkou(request):





  




     #return redirect("userindex.hmtl")

# Create your views here.

 