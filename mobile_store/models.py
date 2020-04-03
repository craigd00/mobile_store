from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from tango_with_django_project import settings
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.db.models.signals import post_save

# Create your models here.
CATEGORY_CHOICES = (
    ('AP', 'Apple'),
    ('AN', 'Android')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)
    
#model for the contact 
class Contact(models.Model):
    NAME_MAX_LENGTH = 128
    FEEDBACK_MAX_LENGTH = 200

    firstname = models.CharField(max_length=NAME_MAX_LENGTH)
    surname = models.CharField(max_length=NAME_MAX_LENGTH)
    email = models.EmailField(blank=True)
    feedback = models.CharField(max_length=FEEDBACK_MAX_LENGTH, blank=True)
    def save(self, *args, **kwargs):
       
        super(Contact, self).save(*args, **kwargs)

class Review(models.Model):
    PHONE_MAX_LENGTH = 100
    REVIEW_MAX_LENGTH = 300
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, default="user")
    phone = models.CharField(max_length=PHONE_MAX_LENGTH)
    review = models.CharField(max_length=REVIEW_MAX_LENGTH, blank=True)
    rating = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
       
        super(Review, self).save(*args, **kwargs)

#model for items 
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='AP')
    slug = models.SlugField(default="product")
    description = models.TextField(default="Description unavailable for this product")
    image = models.CharField(default="sale.jpg", max_length=400)   
    
    #gets the static url of the image to use in templates
    def get_static_url(self):
       return settings.STATIC_URL + 'images/' + self.image

    def __str__(self):
        return self.title

    #gets absolute url of item
    def get_absolute_url(self):
        return reverse('mobile_store:product', kwargs={
            'slug':self.slug
        })

    #adds item to basket using add to basket view
    def get_add_to_basket_url(self):
        return reverse('mobile_store:add_to_basket', kwargs={
            'slug':self.slug
        })
    
    #removes item from basket using remove from basket view
    def get_remove_from_basket_url(self):
        return reverse('mobile_store:remove_from_basket', kwargs={
            'slug':self.slug
        })


#model used when someone has item in basket
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    #gets price of item multiplied by quantity
    def get_total_item_price(self):
        return self.quantity * self.item.price

    #gets discount price of item if it has one
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    #if item has a discount price it uses that, otherwise it returns the normal price
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


#model for an order from a user, can add many items to order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField() 
    items = models.ManyToManyField(OrderItem)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    #gets order
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    
# model for the billing address of the user including the country field
class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip=models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username

class Review(models.Model):
    PHONE_MAX_LENGTH = 100
    REVIEW_MAX_LENGTH = 300
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, default="user")
    phone = models.CharField(max_length=PHONE_MAX_LENGTH)
    review = models.CharField(max_length=REVIEW_MAX_LENGTH, blank=True)
    rating = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
       
        super(Review, self).save(*args, **kwargs)
        





    




    
