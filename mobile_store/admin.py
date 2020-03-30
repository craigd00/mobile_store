from django.contrib import admin
from mobile_store.models import Category, Page
from mobile_store.models import UserProfile
from mobile_store.models import Contact
from mobile_store.models import Item, OrderItem, Order

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)  
admin.site.register(Contact) 
admin.site.register(Item) 
admin.site.register(Order) 
admin.site.register(OrderItem) 

