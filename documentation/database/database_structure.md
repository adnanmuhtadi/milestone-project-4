<h1 align="center">Database Structure</h1>

The User model used in this project is provided by Django which came from the Code Institute 'Boutique Ado' video tutorials as a part of defaults `django.contrib.auth.models`. For more information about [click here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

# Data Modelling

## Profile App

### Profile

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
User | user | OneToOneField 'User' | on_delete=models.CASCADE
Phone Number | phone_number | CharField  | max_length=20, null=True, blank=True
Address Line 1 | address_line_1 | CharField  | max_length=80, null=True, blank=True
Address Line 2 | address_line_2 | CharField  | max_length=80, null=True, blank=True
Town/City | town_or_city | CharField  | max_length=40, null=True, blank=True
County/State | county_state | CharField  |max_length=80, null=True, blank=True
PostCode | postcode | CharField | max_length=20, null=True, blank=True
Country | country | CountryField | blank_label='Country *', null=True, blank=True

## Product App

### Product

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Category | category | Foreign Key 'Category' | null=True, blank=True, on_delete=models.SET_NULL
SKU | sku | CharField | max_length=254, null=True, blank=True
Name | name | CharField | max_length=254
Description | description | TextField | 
Price | price | DecimalField | max_digits=6, decimal_places=2
Colour | colour | CharField | max_length=254, null=True, blank=True
size | size | DecimalField | max_digits=6, decimal_places=0, null=True, blank=False
Has_sizes | has_sizes | BooleanField | default=True, null=True, blank=True
Has_sold | has_sold | BooleanField | default=False, null=True, blank=True
Image_url | image_url | URLField | max_length=1024, null=True, blank=True
Image | image | ImageField | null=True, blank=True
Image_two_url | image_two_url | URLField | max_length=1024, null=True, blank=True
Image_two | image_two | ImageField | null=True, blank=True
Image_three_url | image_three_url | URLField | max_length=1024, null=True, blank=True
Image_three | image_three | ImageField | null=True, blank=True
Image_four_url | image_four_url | URLField | max_length=1024, null=True, blank=True
Image_four | image_four | ImageField | null=True, blank=True

### Category

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Name | name | Primary Key, 'Category', CharField | max_length=254 
Readable Name | readable_name | CharField | max_length=254, null=True, blank=True

## Checkout App

### Order

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Order Number | order_number | CharField | max_length=32, null=False, editable=False
Profile | profile | ForeignKey 'Profile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=50, null=False, blank=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone Number | phone_number | CharField | max_length=20, null=False, blank=False
Address Line 1 | address_line_1 | CharField | max_length=80, null=False, blank=False
Address Line 2 | address_line_2 | CharField | max_length=80, null=True, blank=True
Town/City | town_city | CharField | max_length=40, null=False, blank=False
State/County | state_county | CharField | max_length=80, null=True, blank=True
PostCode | postcode | CharField | max_length=20, null=True, blank=True
Country | country | CountryField | blank_label='Country *', null=False, blank=False
Purchase Date | purchase_date | DateTimeField | auto_now_add=True
Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Grand Price | grand_price | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Original Basket | original_basket | TextField | null=False, blank=False, default=''
Stripe Pid | stripe_pid | CharField | null=False, blank=False, default=''

### Order Item Details

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Order | order | Foreign Key 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE
Product Size | product_size | CharField | max_length=2, null=True, blank=True
Product Sold | product_sold | CharField | max_length=2, null=True, blank=True
Quantity | quantity | IntegerField | null=False, blank=False, default=0
Line Item Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

## Home App

### Contact Us

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
User | user | Foreign Key 'User' | on_delete=models.CASCADE, null=True, blank=True
Subject | subject | CharField | max_length=254
Message | message | TextField |
Date | date | DateField | auto_now_add=True
Time | time | TimeField | auto_now_add=True

## Testimonial App

### Testimonial

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
User | user | Foreign Key 'User' | on_delete=models.CASCADE, null=True
Date | date | DateField | auto_now_add=True
Time | time | TimeField | auto_now_add=True
Title | title | CharField | max_length=254
Message | message | TextField | 
Rating | rating | IntegerField | null=True, blank=True, default=0
