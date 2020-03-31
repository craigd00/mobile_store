import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from mobile_store.models import Category, Page
from mobile_store.models import Item

def populate():
    android_pages = [
        {'title': 'Samsung Website',
         'url':'https://www.samsung.com/uk/',
         'views': 20},
        {'title':'Huawei Website',
         'url':'https://www.huawei.com/uk/',
         'views': 38},
        {'title':'Nokia Website',
         'url':'https://www.nokia.com/',
         'views': 64}]

    apple_pages = [
        {'title':'iPhone XR',
         'url':'https://www.apple.com/uk/iphone-11-pro/',
         'views': 12},
        {'title':'iPhone 11 Pro',
         'url':'https://www.apple.com/uk/iphone-11-pro/',
         'views': 2},
        {'title':'Airpods',
         'url':'https://www.apple.com/uk/airpods/',
         'views': 89}]



    cats = {'Android': {'pages': android_pages, 'views':128, 'likes':64},
            'Apple': {'pages': apple_pages, 'views':64, 'likes':32},
        }

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

 

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Mobile Store population script...')
    populate()

    
         
         
         
         
         
