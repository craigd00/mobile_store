import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

from mobile_store.models import Item, Review

def populate():
    add_phone(phone_name='iPhone XR',
        price=559.99,
        discount_price=0,
        brand='Apple',
        label='primary',
        slug='iPhoneXR',
        description='The iPhone X R display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 6.06 inches diagonally (actual viewable area is less). Rated IP67 (maximum depth of 1 metre up to 30 minutes) under IEC standard 60529 A12 Bionic chip',
        image='iphone-xr-black.png')
    
    add_phone(phone_name='Samsung Galaxy 10',
        price=799,
        discount_price=699,
        brand='Android',
        label='primary',
        slug='SamsungGal10',
        description='Completely redesigned to remove interruptions from your view. The Galaxy S10 introduce a stunning new Infinity-O Display. They are crafted from flawless glass which wraps perfectly from edge to edge. They are minimal, beautiful and effortlessly elegant. With no home button, no notch for the receiver and a simple dot opening for the front camera, you will have an uninterrupted viewing experience. They even come with a screen protector to safeguard them against little accidents.',
        image='samsungal10.jpg')

    add_phone(phone_name='Honor 20',
        price=299.99,
        discount_price=0,
        brand='Android',
        label='primary',
        slug='Honor20',
        description='Capture the wonder of lifes best moments with HONOR 20. Featuring an iconic glass design and quad camera system with a 48-megapixel sensor, HONOR 20 is a marvel of smartphone engineering existing where passion, style, and high-performance meet.',
        image='honor20.jpg')

    
    add_phone(phone_name='iPhone 8',
        price=299.99,
        discount_price=154.99,
        brand='Apple',
        label='primary',
        slug='iPhone8',
        description='iPhone 8 and iPhone 8 Plus are splash, water and dust resistant, and were tested under controlled laboratory conditions with a rating of IP67 under IEC standard 60529 (maxiumum depth of 1 metre up to 30 minutes). Splash, water and dust resistance are not permanent conditions and resistance might decrease as a result of normal wear.',
        image='iphone8.jpg')
    
    add_phone(phone_name='Samsung Galaxy S9',
        price=450,
        discount_price=399,
        brand='Android',
        label='primary',
        slug='SamsungGal9',
        description='Samsung Galaxy S9 supports frequency bands GSM, HSPA, LTE. The device is working on an Android 8.0 (Oreo) with a Octa-core (4x2.7 GHz Mongoose M3 & 4x1.8 GHz Cortex-A55) - EMEAOcta-core (4x2.7 GHz Kryo 385 Gold & 4x1.7 GHz Kryo 385 Silver) - USA & China processor and 4 GB RAM memory. Samsung Galaxy S9 has 64/128/256 GB of internal memory.',
        image='samgals9.jpg')

    add_phone(phone_name='Google Pixel',
        price=275.99,
        discount_price=0,
        brand='Android',
        label='primary',
        slug='GooglePixel',
        description='This device has a Qualcomm SDM845 Snapdragon 845 (10 nm) chipset. The main screen size is display size 5.5 inches, 76.7 cm2  with 1080 x 2160 pixels, 18:9 ratio  resolution. It has a 443 ppi density) ppi pixel density. The screen covers about 77.2 percent of the device body.',
        image='googlepixel.jpg')

    add_phone(phone_name='iPhone X',
        price=450,
        discount_price=0,
        brand='Apple',
        label='primary',
        slug='iPhoneX',
        description='The sharpest display ever on an iPhone. The iPhone X features a colorful OLED display with more... Also includes facial recognition. You can register your face with the iPhone X so that it automatically unlocks. Animoji is live! This ties in to facial recognition but is extremely fun',
        image='iphone10.jpg')

    add_phone(phone_name='Samsung Galaxy S8',
        price=250,
        discount_price=199.99,
        brand='Android',
        label='primary',
        slug='SamsungGal8',
        description='Samsung Galaxy S8 supports frequency bands GSM, HSPA, LTE. The device is working on an Android OS, v7.0 with a Octa-core (4x2.35 GHz Kryo & 4x1.9 GHz Kryo) - US modelOcta-core (4x2.3 GHz & 4x1.7 GHz) - EMEA processor and  4 GB RAM memory. Samsung Galaxy S8 has 64 GB of internal memory. This device has a Qualcomm MSM8998 Snapdragon 835 - US modelExynos 8895 Octa - EMEA chipset.',
        image='samgals8.jpg')

    add_phone(phone_name='LG Stylo 2',
        price=100,
        discount_price=62.99,
        brand='Android',
        label='primary',
        slug='LGStylo2',
        description='The device is working on an Android OS, v6.0 (Marshmallow) with a Quad-core 1.2 GHz Cortex-A53 processor and  2 GB RAM memory. LG Stylo 2 has 16 GB of internal memory. This device has a Qualcomm MSM8916 Snapdragon 410 chipset. The main screen size is 5.7 inches with 720 x 1280 pixels resolution. It has a 258 ppi pixel density.',
        image='lgstylo2jpg.jpg')


    add_phone(phone_name='Sony Xperia T3',
        price=74.99,
        discount_price=0,
        brand='Android',
        label='primary',
        slug='SonyXperiaT3',
        description='Sony Xperia T3 has 8 GB of internal memory. This device has a Qualcomm MSM8928-2 Snapdragon 400 (D5103/D5106)/ Qualcomm MSM8228 (D5102) chipset. The main screen size is 5.3 inches  with 720 x 1280 pixels  resolution. It has a 277  ppi pixel density. The screen covers about 66.7 percent of the body',
        image='sonyxperiaT3.jpg')


    add_phone(phone_name='iPhone 9',
        price=450,
        discount_price=389.99,
        brand='Apple',
        label='primary',
        slug='iPhone9',
        description='Apple iPhone 9 smartphone runs on iOS v11 operating system. The phone is powered by Octa core processor. It has 4 GB RAM and 64 GB internal storage. Apple iPhone 9 smartphone has a OLED display. The screen has a resolution of 750 x 1334 pixels and 294 ppi pixel density. On camera front, the buyers get a 7 MP Front Camera.',
        image='iphone9.png')


    
    add_phone(phone_name='Huawei P20',
        price=299.99,
        discount_price=221.99,
        brand='Android',
        label='primary',
        slug='HuaweiP20',
        description='The Huawei P20 Pro is a phone that stands out with its large, spacious display and its triple camera at the back. Its huge screen occupies most of its front, with a notch at the top housing the earpiece and front-facing camera. The triple camera arrangement is comprised of a massive, 40MP camera for regular shots.',
        image='huaweip20.jpg')
           
    add_phone(phone_name='iPhone 7',
        price=150.99,
        discount_price=0,
        brand='Apple',
        label='primary',
        slug='iPhone7',
        description='One of the key new features in the iPhone 7 involves a switch from the existing headphone jack to the smartphones existing Lightning connector for headphone use, which enables the iPhone 7 to be the thinnest iPhone yet — as well as make the phone more water resistant. In addition to the Lightning-based EarPods, Apple will also be releasing wireless Apple AirPods as an option for iPhone 7 users.',
        image='iphone7.jpg')

    add_phone(phone_name='Samsung Note 10',
        price=564.99,
        discount_price=0,
        brand='Android',
        label='primary',
        slug='SamsungNote10',
        description='With Galaxy Note10 and Note10+ we have designed a mobile experience that is like a computer, a gaming console, a movie-tech camera, and an intelligent pen, all in one device. More screen, less interruption. Now comes in two sizes: powerful and powerful.For the first time ever, you can choose the Note size that fits you best. Impossibly thin design: High-polish metal and glass meld seamlessly - all in an impressively slim design. Cinematic Infinity-O Display. More power. More speed. More storage',
        image='samnote10.png')

    add_review(name = 'John',
    phone='iPhone 8',
    review='Reliable phone, could not ask for much more',
    rating = 8)

    add_review(name = 'John',
    phone='Samsung Galaxy 8',
    review='Low battery life, price was quite expensive for product',
    rating = 3)

#populates the phones by passing in what they need to be created   
def add_phone(phone_name, price, discount_price, brand, label, slug, description, image):
    p = Item.objects.get_or_create(phone_name=phone_name, 
    price=price, discount_price=discount_price, brand=brand, 
    label=label, slug=slug, description=description, image=image)[0]
    return p

def add_review(name, phone, review, rating):
    r = Review.objects.get_or_create(name=name, 
    phone=phone, review=review, rating=rating)[0]
    return r


if __name__ == '__main__':
    print('Starting Mobile Store population script...')
    populate()

    
         
         
         
         
         
