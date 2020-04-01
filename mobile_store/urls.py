from django.urls import path
from mobile_store import views


app_name = 'mobile_store'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('basket/', views.basket, name='basket'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
   # path('register/', views.register, name='register'),
   # path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('apple/', views.AppleView.as_view(), name='apple'),
    path('android/', views.AndroidView.as_view(), name='android'),
    path('iphoneXR/', views.iphoneXR, name='iphoneXR'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('contacting_us/', views.contacting_us, name='contacting_us'),
    path('reviews/', views.reviews, name='reviews'),
    path('checkout_page/', views.checkout_page, name='checkout_page'),
    path('order_summary/', views.OrderSummaryView.as_view(), name='order_summary'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('add_to_basket/<slug>/', views.add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<slug>/', views.remove_from_basket, name='remove_from_basket'),    
    path('remove_single_item_from_basket/<slug>/', views.remove_single_item_from_basket, name='remove_single_item_from_basket'),
    #path('logout/', views.user_logout, name='logout'),
    #path('search/', views.search, name='search'),
]
