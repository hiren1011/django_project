from django.urls import path,include
from app1.views import delete_product_view,add_product_view,edit_product_view, hello,contact, logout_view, search_view, signup , signin_view,about,home,product_view,products

urlpatterns = [
    path('hello/', hello ),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('signup/',signup , name='signup'),
    path('signin/',signin_view, name='signin'),
    path('products/',products,name="products_url"),
    path('products/<int:no>',product_view,name='product_url'),
    path('edit-product/<int:no>',edit_product_view,name='edit_product'), 
    path('delete-product/<int:no>',delete_product_view,name='delete_product'), 
    path('delete-product/<int:no>/?delete=true',delete_product_view,name='delete_product'), 
    path('add-product/',add_product_view,name='add_product'),

    path('logout/',logout_view,name='logout')
    
]
