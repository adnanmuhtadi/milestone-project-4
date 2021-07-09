<h1 align="center">Database Structure</h1>

The User model used in this project is provided by Django which came from the Code Institute 'Boutique Ado' video tutorials as a part of defaults `django.contrib.auth.models`. For more information about [Click here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

# Data Modelling

## Profile App

### Profile

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
User | profile_user | Primary Key, OneToOneField 'User' | 
Full Name | profile_full_name | CharField  | 
Phone Number | profile_phone_number | CharField  | 
Address Line 1 | profile_address_line_1 | CharField  | 
Address Line 2 | profile_address_line_2 | CharField  | 
Town/City | profile_town_city | CharField  | 
County/State | profile_county_state | CharField  |
PostCode | profile_postcode | CharField | 
Country | profile_country | CountryField | 

### Product

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Category | category | Foreign Key 'Category' | null=True, blank=True, on_delete=models.SET_NULL
Name | product_name | CharField | max_length=254
SKU | product_sku | CharField | max_length=254
Description | product_description | TextField | 
Price | product_price | DecimalField | max_digits=6, decimal_places=2
Colour | product_colour | CharField | max_length=254, null=True, blank=True
size | product_size | Int | 
Image_url | product_image_url | URL | max_length=1024, null=True, blank=True
Image | product_image | ImageField | null=True, blank=True

### Category

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Name | category_name | Primary Key, 'Category', CharField | max_length=254 
Readable Name | readable_name | CharField | max_length=254, null=True, blank=True

## Checkout App

### Order

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Order Number | order_order_number | CharField | 
Profile | order_profile | ForeignKey 'Profile' | 
Full Name | order_full_name | CharField | 
Email | order_email | EmailField | 
Phone Number | order_phone_number | CharField | 
Address Line 1 | order_address_line_1 | CharField |
Address Line 2 | order_address_line_2 | CharField |
Town/City | order_town_city | CharField |
State/County | order_state_county | CharField |
PostCode | order_postcode | CharField |
Country | order_country | CountryField |
Purchase Date | order_purchase_date | DateTimeField | 
Delivery Cost | order_delivery_cost | DecimalField | 
Order Total | order_order_total | DecimalField | 
Grand Total | order_grand_total | DecimalField | 

### Order Item Details

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
Order | order_item_order | Foreign Key 'order_number, CharField | 
Product | order_item_product | ForeignKey 'Product', CharField | 
Product Total | order_item_product_total | DecimalTotal | 
Order Date | order_item_order_date | DateTimeField  | 

## Testimonial App

### Testimonial

Name | Database Key | Field Type | Validation
------------ | ------------- | ------------- | -------------
User | testimonial_user | Foreign Key 'Profile', CharField | 
Message | testimonial_message | TextField 
Date | testimonial_Date | DateTimeField |