from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    NAME_MAX_LENGTH = 128
    FEEDBACK_MAX_LENGTH = 200

    firstname = models.CharField(max_length=NAME_MAX_LENGTH)
    surname = models.CharField(max_length=NAME_MAX_LENGTH)
    email = models.EmailField(blank=True)
    feedback = models.CharField(max_length=FEEDBACK_MAX_LENGTH, blank=True)

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#class Phone(models.Model):
    #PHONE_MAX_LENGTH = 200
    #DESC_MAX_LENGTH = 400

    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #picture1 = models.ImageField(upload_to='static/images', blank=True)
    #picture2 = models.ImageField(upload_to='static/images', blank=True)
    #picture3 = models.ImageField(upload_to='static/images', blank=True)
    #phone_name = models.CharField(max_length=PHONE_MAX_LENGTH)
    #description = models.CharField(max_length=DESC_MAX_LENGTH, blank=True)
    #price = models.IntegerField(default=0)

    #def __str__(self):
        #return self.phone_name

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    
    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField() 
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username




    
