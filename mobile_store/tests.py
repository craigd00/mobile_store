from django.test import TestCase

# Create your tests here.
import os
import mobile_store.models
from django.db import models
from mobile_store.models import Contact, Item, OrderItem, Order, Review
from tango_with_django_project import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields
from mobile_store import forms
from population_script import populate

class ItemTestsNames(TestCase):
    #tests items are what they say they are
    def test_for_price_equal(self):

        phone = Item(phone_name='test', price = 200, discount_price=0,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.price == 200), True)

    def test_for_discount_is_zero(self):

        phone = Item(phone_name='test', price = 200, discount_price=0,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.discount_price == 0), True)

    def test_for_discount_is_greater_zero(self):

        phone = Item(phone_name='test', price = 200, discount_price=50,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.discount_price > 0), True)

    def test_for_phone_name_correct(self):

        phone = Item(phone_name='test', price = 200, discount_price=50,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.phone_name == "test"), True)

    def test_for_brand_correct(self):

        phone = Item(phone_name='test', price = 200, discount_price=50,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.brand != "Apple"), False)

    def test_for_slug_correct(self):

        phone = Item(phone_name='test', price = 200, discount_price=50,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.slug == "testproduct"), True)

    def test_for_description_correct(self):

        phone = Item(phone_name='test', price = 200, discount_price=50,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.description == "great product"), True)

    def test_for_image_correct(self):

        phone = Item(phone_name='test', price = 200, discount_price=50,
        label='primary', brand='Apple', slug='testproduct', 
        description='great product', image='mobile_store.png')
        self.assertEqual((phone.image == "mobile_store.png"), True)

 

class SettingsTest(TestCase):
    'checks features in settings exist'

    def test_installed_authorisation(self):
        self.assertTrue('registration' in settings.INSTALLED_APPS)  
    
    def test_installed_crispy_forms(self):
        self.assertTrue('crispy_forms' in settings.INSTALLED_APPS)

    def test_email_host(self):
        self.assertEqual(('mobilestoregu@gmail.com' == settings.EMAIL_HOST_USER), True)

class ModelsTest(TestCase):
    #checks models exist

    def test_contact_model(self):
        self.assertTrue('Contact' in dir(mobile_store.models))

    def test_item_model(self):
        self.assertTrue('Item' in dir(mobile_store.models))

    def test_order_model(self):
        self.assertTrue('Order' in dir(mobile_store.models))

    def test_order_item_model(self):
        self.assertTrue('OrderItem' in dir(mobile_store.models))

    def test_review_model(self):
        self.assertTrue('Review' in dir(mobile_store.models))


class FormTests(TestCase):
    #checks that forms exist and so does fields in them 
    def test_contact_form_in_forms(self):

        self.assertTrue('ContactForm' in dir(forms))
    
    def test_contact_form_fields(self):
        contact_form = forms.ContactForm()
        self.assertEqual(type(contact_form.__dict__['instance']), Contact)
        fields = contact_form.fields
        expected_fields = {
            'firstname': django_fields.CharField,
            'surname': django_fields.CharField,
            'email': django_fields.EmailField,
            'feedback': django_fields.CharField,
        }
        for name in expected_fields:
            expected_field = expected_fields[name]
            self.assertTrue(name in fields.keys())
            self.assertEqual(expected_field, type(fields[name]))

    def test_user_form_in_forms(self):

        self.assertTrue('UserForm' in dir(forms))
    
    def test_user_form_fields(self):
        user_form = forms.UserForm()
        self.assertEqual(type(user_form.__dict__['instance']), User)
        fields = user_form.fields
        expected_fields = {
            'username': django_fields.CharField,
            'email': django_fields.EmailField,
            'password': django_fields.CharField,
        }
        for name in expected_fields:
            expected_field = expected_fields[name]
            self.assertTrue(name in fields.keys())
            self.assertEqual(expected_field, type(fields[name]))

    def test_review_form_in_forms(self):

        self.assertTrue('ReviewForm' in dir(forms))
    
    def test_review_form_fields(self):
        review_form = forms.ReviewForm()
        self.assertEqual(type(review_form.__dict__['instance']), Review)
        fields = review_form.fields
        expected_fields = {
            'name': django_fields.CharField,
            'phone': django_fields.CharField,
            'review': django_fields.CharField,
            'rating': django_fields.IntegerField,
        }
        for name in expected_fields:
            expected_field = expected_fields[name]
            self.assertTrue(name in fields.keys())
            self.assertEqual(expected_field, type(fields[name]))

class ViewTesting(TestCase):
    #checks that views exist to these pages
    def test_index_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:index')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/')

    def test_about_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:about')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/about/')

    def test_android_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:android')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/android/')

    def test_apple_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:apple')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/apple/')

    def test_contact_us_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:contact_us')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/contact_us/')

    def test_contacting_us_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:contacting_us')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/contacting_us/')

    
    def test_reviews_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:reviews')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/reviews/')

    def test_viewreviews_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:viewreviews')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/viewreviews/')

    
    def test_checkout_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:checkout_page')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/checkout_page/')

    
    def test_order_summary_view_exists(self):
        url = ''
        try:
            url = reverse('mobile_store:order_summary')

        except:
            pass
        
        self.assertEqual(url, '/mobile_store/order_summary/')

class TemplateTests(TestCase):

    #checks registration templates
    def test_registration_templates(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'registration')
        template_path = os.path.join(template_base_path, 'registration_form.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'registration_closed.html')
        self.assertTrue(os.path.exists(template_path))

    def test_login_templates(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'registration')
        template_path = os.path.join(template_base_path, 'login.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'logout.html')
        self.assertTrue(os.path.exists(template_path))

    def test_password_templates(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'registration')
        template_path = os.path.join(template_base_path, 'password_change_form.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'password_change_done.html')
        self.assertTrue(os.path.exists(template_path))

    #checks mobile store templates
    def test_mobile_store_templates(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'mobile_store')
        template_path = os.path.join(template_base_path, 'about.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'android.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'apple.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'base.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'checkout_page.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'contact_us.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'contacting_us.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'index.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'order_summary.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'product.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'reviews.html')
        self.assertTrue(os.path.exists(template_path))
        template_path = os.path.join(template_base_path, 'viewreviews.html')
        self.assertTrue(os.path.exists(template_path))

    #checks index title
    def test_index_title(self):
        request = self.client.get(reverse('mobile_store:index'))
        content = request.content.decode('utf-8')
        self.assertTrue('Welcome to our Mobile Store! Find your phone!</h1>' in content)

    #check button in contact us 
    def test_button_contact_us(self):
        request = self.client.get(reverse('mobile_store:contact_us'))
        content = request.content.decode('utf-8')
        self.assertTrue('<button class="btn btn-primary" type="submit">Submit your feedback</button>' in content)
        



 