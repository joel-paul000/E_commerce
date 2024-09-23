from django.urls import path
from UserApp import views

urlpatterns =[
    path('',views.login,name='login'),
    path('ind',views.ind,name='ind'),
    #path('login',views.login,name='login'),
    path('reg',views.regist,name="reg"),
    path("cate1",views.cat,name='cate1'),
    path('cart/<int:sample_id>',views.cart,name='cart'),
    path('checkoutpro',views.checkoutpro,name='checkoutpro'),
    path('confirmation',views.confirmation,name='confirmation'),
    path("viewmore/<int:sample_id>",views.viewmore,name='viewmore'),
    path('addcart/<int:product_id>',views.store,name='addcart'),
    path("deletecart/<int:sample_id>",views.deletecart,name='deletecart'),
    path('viewcart',views.viewcart,name="viewcart"),
    path('catt',views.catt,name="catt"),
    path('viewcateogories/<int:id>',views.viewcateogories,name="viewcateogories"),
    path('buyedproduct/<int:sample_id>',views.buyedproducts,name="buyedproduct"),
    path('viewbuyed',views.viewbuyed,name="viewbuyed"),
    path('buyed/<int:product_id>',views.buyed,name="buyed"),
    path("logout",views.logout,name='logout'),
    path('userprofile',views.userprofile,name="userprofile"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    #path('check',views.check,name="check"),
    path("checkouttt",views.checkouttt,name="checkoutt"),

  
   
    
    
]