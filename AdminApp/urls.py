from django.urls import path
from .import views

urlpatterns = [
    path('hey',views.hey,name='hey'),
    path('index',views.index,name='index'),
    path('cateo',views.cateogory,name="cateo"),
    path("product",views.product,name="product"),
    path('viewcat',views.viewcat,name="viewcat"),
    path("viewpro",views.viewpro,name="viewpro"),
    path("delete/<int:sample_id>",views.delete,name="delete"),
    path("deletepro/<int:sample_id>",views.deletepro,name="deletepro"),
    path("updatecateogory/<int:sample_id>",views.updatecateogory,name='updatecateogory'),
    path("store/<int:sample_id>",views.store,name="store"),
    path("updateproduct/<int:sample_id>",views.updateproduct,name='updateproduct'),
    path("productstore/<int:sample_id>",views.productstore,name="productstore"),
    path("viewcustomer",views.viewcustomer,name='viewcustomer'),
    path("deletecus/<int:sample_id>",views.deletecus,name="deletecus"),
    path("vieworder",views.vieworder,name="vieworder"),
    path("deleteorder/<int:sample_id>",views.deleteorder,name="deleteorder"),
    path('logoutadmin',views.logoutadmin,name="logoutadmin")



]