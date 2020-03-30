from django import forms
from mobile_store.models import Page, Category
from django.contrib.auth.models import User
from mobile_store.models import UserProfile
from mobile_store.models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.ModelForm):
    firstname= forms.CharField(max_length=Contact.NAME_MAX_LENGTH, label="First Name")
    surname= forms.CharField(max_length=Contact.NAME_MAX_LENGTH, label="Surname")
    email= forms.EmailField(max_length=500, label="Email")
    feedback= forms.CharField(label='', max_length=Contact.FEEDBACK_MAX_LENGTH, widget=forms.Textarea(attrs={'placeholder': 'Enter your feedback here'}))

    class Meta:
        model = Contact
        fields = ('firstname', 'surname', 'email', 'feedback',)
    



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


