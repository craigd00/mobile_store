from django.urls import path

from . import views
from mobile_store import views

from .views import (
    CheckoutView
    )


app_name = 'mobile_store'

urlpatterns = [

    path('', views.homeView, name='index'),
    path('about/', views.about, name='about'),
    path('apple/', views.AppleView.as_view(), name='apple'),
    path('android/', views.AndroidView.as_view(), name='android'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('contacting_us/', views.contacting_us, name='contacting_us'),
    path('reviews/', views.reviews, name='reviews'),
    path('viewreviews/', views.viewreviews, name='viewreviews'),
    path('checkout_page/', CheckoutView.as_view(), name='checkout_page'),
    path('order_summary/', views.OrderSummaryView.as_view(), name='order_summary'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('add_to_basket/<slug>/', views.add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<slug>/', views.remove_from_basket, name='remove_from_basket'),    
    path('remove_single_item_from_basket/<slug>/', views.remove_single_item_from_basket, name='remove_single_item_from_basket'),
]
