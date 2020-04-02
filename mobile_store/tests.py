from django.test import TestCase

# Create your tests here.
from mobile_store.models import Item
from django.db import models
from django.conf import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields

class ItemTestsNames(TestCase):
    def test_for_price_equal(self):

        item = Item(title='test', price = 200, discount_price=0,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.price == 200), True)

    def test_for_discount_is_zero(self):

        item = Item(title='test', price = 200, discount_price=0,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.discount_price == 0), True)

    def test_for_discount_is_greater_zero(self):

        item = Item(title='test', price = 200, discount_price=50,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.discount_price > 0), True)

    def test_for_title_correct(self):

        item = Item(title='test', price = 200, discount_price=50,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.title == "test"), True)

    def test_for_category_correct(self):

        item = Item(title='test', price = 200, discount_price=50,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.category != "Apple"), False)

    def test_for_slug_correct(self):

        item = Item(title='test', price = 200, discount_price=50,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.slug == "testproduct"), True)

    def test_for_description_correct(self):

        item = Item(title='test', price = 200, discount_price=50,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.description == "great product"), True)

    def test_for_image_correct(self):

        item = Item(title='test', price = 200, discount_price=50,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.image == "mobile_store.png"), True)

    def test_for_image_static_correct(self):

        item = Item(title='test', price = 200, discount_price=50,
        label='primary', category='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((item.get_static_url == "{% static 'images/mobile_store.png %}"), True)
