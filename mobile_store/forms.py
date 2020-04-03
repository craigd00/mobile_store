from django import forms

from django.contrib.auth.models import User
from mobile_store.models import Contact, Review

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

class ReviewForm(forms.ModelForm):
 
    name = forms.CharField(max_length=Contact.NAME_MAX_LENGTH, label="Name")
    phone = forms.CharField(max_length=Review.PHONE_MAX_LENGTH,label="Phone")
    review = forms.CharField(label='', max_length=Review.REVIEW_MAX_LENGTH, widget=forms.Textarea(attrs={'placeholder': 'Enter your review here'}))
    rating = forms.IntegerField(label="Rating")

    class Meta:
        model = Review
        fields = ('name', 'phone', 'review', 'rating',)




