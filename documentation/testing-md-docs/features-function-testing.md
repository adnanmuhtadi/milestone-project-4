<h1 align="center">Feature, Functional & Useability Testing</h1>

I will be testing all my functions and features within each section of my site and ensuring that it is useable across different browsers which are as follows: Chrome, Edge and Firefox. The devices I would be using to run the tests are as follows: 13inch Macbook Pro, 10.2 inch iPad and 6.5 inch iPhone Pro Max.

A pass would mean that the feature that I am testing has been run on the said browsers and devices, in a situation one of the browsers and/or devices has an issue, it would be considered as a fail.

## Navigation Bar

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Navigation bar | Navigation bar is fixed when going through the site | :heavy_check_mark: |
Search bar| Search bar to redirect you to the product page with what has been searched | :heavy_check_mark: |
Search bar| Searches with titles of the products that match the search criteria | :heavy_check_mark: |
Search bar| Searches with the description of the products that match the search criteria | :heavy_check_mark: |
Navigation bar links | All links in the navigation bar directs you to the appropriate page | :heavy_check_mark: |
Navigation for Admin | When logged in as admin, when selecting 'My Accout' an option to add products would be available | :heavy_check_mark: |
Responsive navigation bar | Burger menu bar expands when selected and displays all options that are in the full-screen | :heavy_check_mark: |

## Footer

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Other Links | When clicked, it would direct the user to the appropriate site | :heavy_check_mark: |
Social links | When clicked, to be directed to the social media web pages | :heavy_check_mark: |
Responsive design | The design to change on smaller screens and have | :heavy_check_mark: |

## Home Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Carousel | Images to rotate with a button associated with different types of products | :heavy_check_mark: | 
Testimonials | Displayed the newest 3 testimonials left by users | :heavy_check_mark: | 
Responsive design | Design of the page changes depending on the screen size | :heavy_check_mark: | 

## Registration

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Sign in page | Sign in page accessible from the registration from | :heavy_check_mark: |
Form | To be able to enter information in form | :heavy_check_mark: |
Email field | If the field does not have an @, a message would appear | :heavy_check_mark: |
Email confirmation field | If the email does not match with the field above, a message would appear  | :heavy_check_mark: |
Username | The ability to add text to the field | :heavy_check_mark: |
Password | The password would need to have more than 8 characters | :heavy_check_mark: |
Confirm Password | Password would need to match the password field | :heavy_check_mark: | 
Email verification | An email to be sent to the email provided with a verification link that the user would need to click on to be fully verified | :heavy_check_mark: | 

## Login

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Page Access | If the user is not logged in, the user would get redirected to the login page with a flash message | :heavy_check_mark: |
Username/email | If the username or email inserted is wrong, an error message would appear | :heavy_check_mark: |
Password | If the password inserted is wrong, an error message would appear | :heavy_check_mark: |
Sign up | If the user does not have a login, the option to sign up is available and redirects the user to the signup page | :heavy_check_mark: |

## Logout

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Confirmation before sign out | When the option of sign out is selected, a page load | :heavy_check_mark: |
Logout | Account logs out once confirmed | :heavy_check_mark: | 

## Returns & Refunds / Privacy / T&C's
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Page load | Pages load as expected | :heavy_check_mark: |

## About
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Google API | Google Maps to be displayed on the page with the location configured | :heavy_check_mark: |

## My Profile
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------


## Testimonial
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Display all testimonials | All testimonials displayed from newest to oldest | :heavy_check_mark: |
Name of User | The name of the user who posted the testimonial would be showing on the testimonial |
Sorting testimonials | All testimonials displayed from newest to oldest | :heavy_check_mark: |
Sorting | Sorting would change depending on the user selection on how they would like to have it sorted | :heavy_check_mark: | 
Rating | If the rating is between 1 - 5, stars would be a representative of the number displayed | :heavy_check_mark: | 
Standard User Amends | The owner of the testimonial would be able to either edit and/or delete the testimonial they have posted | :heavy_check_mark: | 
Superuser Amends | The superuser has the power to edit and/or delete any testimonial made by anyone | :heavy_check_mark: | 
Superuser Django Admin | When logging into admin, there would be a section where you would be able to see all the testimonials 

## Add Testimonial
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Add text in all fields | User can insert text in all fields | :heavy_check_mark: |
Missing fields | If the subject or message field is missed, an error message would appear | :heavy_check_mark: |
Rating field | Only add a number up to 5 | | :x:

## Edit Testimonial
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Retrieve testimonial | Retrieving all the information from the review and displaying it in its appropriate placeholder | :heavy_check_mark: |
Missing fields | If the subject or message field is missed, an error message would appear | :heavy_check_mark: |
Add text in all fields | User can insert text in all fields | :heavy_check_mark: |
Rating field | Only add a number up to 5 | | :x:

## Products
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Displaying Products | All products displayed in a card format with the details underneath each product | :heavy_check_mark: |
Number of Products | The number of displayed products available | :heavy_check_mark: |
Number of search products | When you search "Adidas" in the search bar, the number of products it is returned has updated in the product count | :heavy_check_mark: | 
Add to Basket | When clicked on, the subtotal of the shoes would be updated in the basket | :heavy_check_mark: |
Sold Products | When a pair of shoes have been sold, a SOLD sign in red would be under the product name and hiding the 'Add to Basket' button  | :heavy_check_mark: |
Superuser Permissions | Edit/Delete option would be available for each product but only for superuser accounts | :heavy_check_mark: |
Product Details | When you click on the image of the product, that would take you to the details of the product | :heavy_check_mark: |

## Product Details 
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Product Details | Have the product details displaying the name, code, price, colour, category, size and description of the product  | :heavy_check_mark: |
Product Image | An enlarged image displayed on the screen | :heavy_check_mark: |
Multiple Product Images | Different images available of the product are selectable and would replace the large image with the image clicked on | :heavy_check_mark: |
Category redirect | When you select the category, it would relocate you to the chosen category | :heavy_check_mark: |
Carry On Shopping | When the button carry on shopping is clicked, it would redirect you back to the product page | :heavy_check_mark: |
Add to basket | When clicked on, the subtotal of the shoes would be updated in the basket | :heavy_check_mark: |
Superuser Permissions | Edit/Delete option would be available for the product but only for superuser accounts | :heavy_check_mark: |

## Add Product Details 
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------


## Edit Product Details 
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------


## Basket 
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Order summary

## Checkout 
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------


## Checkout success 
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------


## Contact Us
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
All fields for logged-in user | The username and email is automatically populated when trying to contact the site admin | :heavy_check_mark: |
All fields for guest users | The username is replaced with full name is automatically populated when trying to contact the site admin | :heavy_check_mark: |
Redirect | Once an email has been sent, the user would be relocated to the home page | :heavy_check_mark: |
Django Admin | Once the email has been sent, The subject and email would be saved to Django admin | :heavy_check_mark: |

## Toasts 
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------


## Emails  
Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------


[Return to main README.md](https://github.com/adnanmuhtadi/milestone-project-4)