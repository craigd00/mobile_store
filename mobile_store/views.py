from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from mobile_store.models import Item, Order, OrderItem, Review
from mobile_store.forms import ContactForm, UserForm, ReviewForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from django.core.mail import EmailMessage   
from django.template.loader import get_template
from django.core.mail import send_mail  #used to email customer
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.core.paginator import Paginator

#ListView used as showing objects on the html page
class HomeView(ListView):
    model = Item
    paginate_by = 8 #used to show how many phones to show on home page
    template_name = 'mobile_store/index.html'

def homeView(request):
    phones = Item.objects.all()
    searchTerm = ''

    if 'search' in request.GET:
        searchTerm = request.GET['search']
        phones = phones.filter(title__icontains=searchTerm)

    if 'type' in request.GET:
        if request.GET.get('type') == "all":
            phones = Item.objects.all()
        else:
            phones = Item.objects.filter(category=request.GET.get('type'))


    paginator = Paginator(phones, 8)
    page = request.GET.get('page')
    phones = paginator.get_page(page)

    get_copy = request.GET.copy()
    params = get_copy.pop('page', True) and get_copy.urlencode()

    context_dict = {'phones': phones, 'searchTerm':searchTerm, 'parameters': params}

    return render(request, 'mobile_store/index.html', context=context_dict)


class AppleView(ListView):
    model = Item
    template_name = 'mobile_store/apple.html'
    paginate_by = 4

    #only shows the phones with the category apple    
    def get(self, request):
        context_dict = {}
        cat = "Apple"
        context_dict['item_list'] = Item.objects.filter(category=cat)
        

        return render(request, 'mobile_store/apple.html', context=context_dict)


class AndroidView(ListView):
    model = Item
    paginate_by = 4
    template_name = 'mobile_store/android.html'

    #only shows the phones with the category android  
    def get(self, request):
        context_dict = {}
        cat = "Android"
        context_dict['item_list'] = Item.objects.filter(category=cat)

        return render(request, 'mobile_store/android.html',context=context_dict)

#shows the order summary, if user does not have an order, will send a message
class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context_dict = {
                'object':order
            }
            
            return render(self.request, 'mobile_store/order_summary.html', context=context_dict)
        except ObjectDoesNotExist:
            messages.error(self.request, "There is no active order")
            return redirect('/')


#def product(request):
   # context_dict = {
      #  'items': Item.objects.all()
   # }
   # return render(request, 'mobile_store/product.html', context=context_dict)

#used for showing products
class ItemDetailView(DetailView):
    model = Item
    template_name = 'mobile_store/product.html'

#adds a phone to the basket
@login_required
def add_to_basket(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item,created = OrderItem.objects.get_or_create(item=item
    , user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Quantity of this item has been added")
            return redirect('mobile_store:order_summary')
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to basket")
            
            return redirect('mobile_store:order_summary')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to basket")
        return redirect('mobile_store:order_summary')


#removes whole item from basket,even if quantity > 1, gives user alerts
@login_required
def remove_from_basket(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from basket")
            return redirect('mobile_store:order_summary')
        else:
        
            messages.info(request, "This item was not in basket")
            return redirect('mobile_store:product', slug=slug)
    else:
   
        messages.info(request, "No current order")
        return redirect('mobile_store:product', slug=slug)

#removes one items quantity from the basket
@login_required
def remove_single_item_from_basket(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()

            else:
                order.items.remove(order_item)

            messages.info(request, "Quantity of this item has been decreased")
            return redirect('mobile_store:order_summary')
        else:
        
            messages.info(request, "This item was not in basket")
            return redirect('mobile_store:product', slug=slug)
    else:
   
        messages.info(request, "No current order")
        return redirect('mobile_store:product', slug=slug)


#takes to checkout page
def checkout_page(request):
    return render(request, 'mobile_store/checkout_page.html')
    

def about(request):
    return render(request, 'mobile_store/about.html')



#views for contacting the website, sends automated email back to client
def contact_us(request):
    form = ContactForm        
    context_dict = {}


    form= ContactForm(request.POST or None)
    if form.is_valid():
        
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')

        contact = form.save(commit=False)
        contact.firstname = firstname
        contact.surname = surname
        contact.email = email
        contact.feedback = feedback
        contact.save()

        subject = "comment"
        comment= firstname + " with the email, " + email + ", sent the following message:\n\n" + feedback + ". We will get back to your message in due course.\n\n" + "Best wishes from the Mobile Store Team";
        send_mail(subject, comment, 'mobilestoregu@gmail.com', [email])


        context_dict['firstname'] = firstname
        context_dict['surname'] = surname
        context_dict['email'] = email
        context_dict['feedback'] = feedback
        #after it emails customer who gave feedback, takes them to different page
        return render(request, 'mobile_store/contacting_us.html', context=context_dict)

    else:
        context =  {'form': form}
        return render(request, 'mobile_store/contact_us.html', context) 
            
#after user has given feedback, they are thanked for the feedback
def contacting_us(request):
    firstname = request.POST.get('firstname')
    context_dict = {
        'firstname':firstname}
    return render(request, 'mobile_store/contacting_us.html', context=context_dict)

@login_required
def reviews(request):
    form = ReviewForm        
    context_dict = {}


    form= ReviewForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        review = request.POST.get('review')
        rating = request.POST.get('rating')

        post = form.save(commit=False)
        post.name = name
        post.phone = phone
        post.review = review
        post.rating = rating
        post.save()
        context_dict['name'] = name
        context_dict['phone'] = phone
        context_dict['review'] = review
        context_dict['rating'] = rating

        return render(request, 'mobile_store/reviews.html')

    else:
        context_dict={
            'form':form
        }
        return render(request, 'mobile_store/reviews.html', context=context_dict) 


@login_required
def viewreviews(request):
    context_dict = {}

    try:
        reviews = Review.objects.all()
        context_dict['reviews'] = reviews
    except Review.DoesNotExist:
        context_dict['reviews'] = None

    return render(request, 'mobile_store/viewreviews.html', context=context_dict)
    
