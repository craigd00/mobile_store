from django import forms
from django import views
from django.contrib.auth.models import User
from mobile_store.models import Contact
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


#form for the contact to submit their feedback using
class ContactForm(forms.ModelForm):
    firstname= forms.CharField(max_length=Contact.NAME_MAX_LENGTH, label="First Name")
    surname= forms.CharField(max_length=Contact.NAME_MAX_LENGTH, label="Surname")
    email= forms.EmailField(max_length=500, label="Email")
    feedback= forms.CharField(label='', max_length=Contact.FEEDBACK_MAX_LENGTH, widget=forms.Textarea(attrs={'placeholder': 'Enter your feedback here'}))

    class Meta:
        model = Contact
        fields = ('firstname', 'surname', 'email', 'feedback',)
    
#using django authentication for login and site authentication
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


#checkout page form for rediriecting to payment method
PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)
class CheckoutForm(forms.Form):
    street_address = forms.CharField()
    apartment_address = forms.CharField(required=False)
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={'class':'custom-select d-block w-100'}))
    zip = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
    
    
    
    
    
    
    
    
    
    
    
    



