from django.contrib import admin

from mobile_store.models import Contact
from mobile_store.models import Item, OrderItem, Order

# Register your models here.
     
admin.site.register(Contact) 
admin.site.register(Item) 
admin.site.register(Order) 
admin.site.register(OrderItem) 

