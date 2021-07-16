<h1 align="center">Database Structure</h1>

The User model used in this project is provided by Django which came from the Code Institute 'Boutique Ado' video tutorials as a part of defaults `django.contrib.auth.models`. For more information about [click here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

# Data Modelling

## Profile App

### Profile

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
User | user | Primary Key, OneToOneField 'User' | 
Full Name | full_name | CharField  | 
Phone Number | phone_number | CharField  | 
Address Line 1 | address_line_1 | CharField  | 
Address Line 2 | address_line_2 | CharField  | 
Town/City | town_city | CharField  | 
County/State | county_state | CharField  |
PostCode | postcode | CharField | 
Country | country | CountryField | 

### Product

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Category | category | Foreign Key 'Category' | null=True, blank=True, on_delete=models.SET_NULL
Name | name | CharField | max_length=254
SKU | sku | CharField | max_length=254
Description | description | TextField | 
Price | price | DecimalField | max_digits=6, decimal_places=2
Colour | colour | CharField | max_length=254, null=True, blank=True
size | size | Int | 
Image_url | image_url | URL | max_length=1024, null=True, blank=True
Image | image | ImageField | null=True, blank=True

### Category

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Name | name | Primary Key, 'Category', CharField | max_length=254 
Readable Name | readable_name | CharField | max_length=254, null=True, blank=True

## Checkout App

### Order

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Order Number | order_number | CharField | 
Profile | profile | ForeignKey 'Profile' | 
Full Name | full_name | CharField | 
Email | email | EmailField | 
Phone Number | phone_number | CharField | 
Address Line 1 | address_line_1 | CharField |
Address Line 2 | address_line_2 | CharField |
Town/City | town_city | CharField |
State/County | state_county | CharField |
PostCode | postcode | CharField |
Country | country | CountryField |
Purchase Date | purchase_date | DateTimeField | 
Delivery Cost | delivery_cost | DecimalField | 
Order Total | order_total | DecimalField | 
Grand Price | grand_price | DecimalField | 

### Order Item Details

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Order | order | Foreign Key 'order_number, CharField | 
Product | product | ForeignKey 'Product', CharField | 
Product Total | product_total | DecimalTotal | 
Order Date | order_date | DateTimeField  | 

## Testimonial App

### Testimonial

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
User | user | Foreign Key 'Profile', CharField | 
Message | message | TextField 
Date | Date | DateTimeField |