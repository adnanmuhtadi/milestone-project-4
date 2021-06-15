<h1 align="center">Milestone Project 4 - Clout Mafia</h1>

[View project here](#)

This eCommerce site is based on advertising and selling exclusive sneakers. The target market audience has a unique market for individuals who have a taste in fashion. Being able to register/login/log out as well as adding/updating/deleting items from the inventory as well as the shopping basket. Giving users the different option of sneakers and sizes as well as being able to search for them to select from depending on availability.

This site would be utilizing Python and Django which was taught from the Code Institute. I will also be using various technologies such as HTML5, CSS3, JQuery and Bootstrap. This project will be responsive and accessible to different size browsers and devices.

<h2 align="center"><img src="#"></h2>

## User Experience (UX)

### The Audience

The intended audience for this project is individuals who are into casual contemporary fashion, namely exclusive designer footwear and streetwear.

### User Objectives

To be able to find and purchase a pair of sneakers easily. Navigate through the site with a consistent layout and structure making the sneakers clear to be seen and accessible. When a pair of sneakers is selected, it will direct the user to a detailed product page, which would display a larger picture of the product, a description and sneaker size.

After having some items added to the basket, to be able to preview the selected sneakers and to see the total price. Once decided to make an order, to be able to go and check out and put in all the card details to purchase the items. To also have the ability to create an account and store the previous orders associated with the account.

Having an additional option to post a testimonial about the service/website to share with other users and having it displayed on the home page to be seen by other users.

### My Objectives

To create a site that would allow a user to register and have a profile on the site. For the user to be able to search for a product and select it to find out more details about it. Within the details page for the user, to be able to select the size that they want and add it to their bag. Having the user then go to checkout and purchase their order.

The site would have a CRUD software architectural style (Create, Read, Update and Delete) for basic operations of persistent storage with the products being added by the admin user. Validation would be included in the site when it comes to adding products, user details and user card details. When a user sends an email to the site admin, to have the subject automatically post to the database for analysing. 

### User Stories

The intended type of users which this website is targeted for are individuals who enjoy online shopping and have a unique taste is fashion.

1. As a user, I want to be able to view a list of products, so that I can purchase one of them.
1. As a user, I want to be able to view the details of an individual item, so I can see the price, description, product image and available size.
1. As a user, I want to be able to sort the sneakers, so I can identify the best priced and alphabetically 
1. As a user, I want to be able to sort a specific category of sneakers, so I can find the specific sneakers I am looking for
1. As a user, I want to be able to search by name and/or description, so I can find sneakers easily
1. As a user, I want to be able to see the number of results that appear from my search, so I can see how many sneakers are available from my search
1. As a user, I want to be able to select the size and quantity of a pair of sneakers, so I can ensure I purchase the right size and amount of my desired order
1. As a user, I want to be able to easily register for an account, so I can have a personal account within the site and be able to view my personal information
1. As a user, I want to be able to recover my password, so I can recover it if needed.
1. As a user, I want to be able to view a personalised profile page, so I can view my personal information as well as my order history
1. As a user, I want to be able to view the overall total of my shopping bag, so I can see my total spending
1. As a user, I want to be able to update my shopping bag at the checkout by updating the quantity of my order, so I can have the option to change my mind if I don’t want to spend as much
1. As a user, I want to be able to easily enter my payment details, so I can easily purchase my items
1. As a user, I want to be able to view an order confirmation after I have purchased my items, so I can verify my purchase order.
1. As a user, I want to be able to post a testimonial, so I can express my opinion of the service/website.
1. As a site owner, I want to be able to add a product, so I can a new pair of sneakers to my store
1. As a site owner, I want to be able to edit, update a product in my store, so I can amend the name, price, description, image and any other product details
1. As a site owner, I want to be able to mark a product as sold when a product has been purchased, so I can ensure it will not be purchased again
1. As a site owner, I want to be able to delete a product, so I can remove the product from my store.
1. As a site owner, I want to be able to see a list of subjects that get used when contacting the site admin, so I can see what user are mostly asking

### Design
-   #### Colour Scheme
    -   The colour scheme I will be working with is mainly black and white to keep it simple and easy on the eyes. The concept is to make the images of the sneakers be the focus of the site.

-   #### Typography
    -   I have chosen to use [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) and [Sarabun](https://fonts.google.com/specimen/Sarabun) 
font as the main fonts throughout the website with Sans Serif as the emergency font in the case for any reason the font is not being imported into the site correctly. Both [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) and [Sarabun](https://fonts.google.com/specimen/Sarabun) are attractive fonts to use as it easy to clear and easy to read. [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) would be used for all the headers of the site where as [Sarabun](https://fonts.google.com/specimen/Sarabun) would be used for the rest of the content

-   #### Imagery
    -   The images that were used as based on the purpose of the site being focused on selling sneakers. All images have been taken personally as I would also be advertising sneakers that have been sold before this project.

*   ### Wireframes

    #### Home Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/home-page.pdf)

    #### Register Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/register-page.pdf)

    #### Login Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/login-page.pdf)

    #### All Products Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/all-products-page.pdf)

    #### Product Details Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/product-details-page.pdf)

    #### Superuser Add/Edit Product Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/superuser-add-edit-product.pdf)

    #### Change Username Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/change-username.pdf)

    #### Change Password Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/change-password.pdf)

    #### Testimonials Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/testimonials-page.pdf)

    #### Shipping & Returns Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/shipping-and-returns-page.pdf)

    #### Privacy Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/privacy-page.pdf)

    #### Terms & Conditions Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/terms-page.pdf)

    #### About Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/about-page.pdf)

    #### Contact Us Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/contact-us-page.pdf)
    
    #### Master Wireframes
    - Master Wireframes - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/clout-mafia-wireframes.bmpr)
    
#### Database Mapping

The database was designed using an online tool called [DB Diagram](https://dbdiagram.io/). The tables where mapped depending on the field requirements.

Database Design - [Mapping](#)

## Features

The features that will be utilised in this project will be as follows:

### Existing Features

#### Site Features

-   

### Features Left to Implement

-   

## Technologies Used

###  Programming Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 was used to structure and present content on my website.
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS3 was used to provide my website with style.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - JavaScript was used to make the site interactive.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - Python was used as the backend language to access and parse data.

### Databases, Frameworks, Libraries, Programs and Templates Used

#### Databases
1. [DB Diagram](https://dbdiagram.io/)
    - Online tool to design the database.
1. [SQLite3:](https://www.sqlite.org/index.html)
    - Database which stores the data to be recalled onto the website.
1. [Heroku Postgresql:](https://www.sqlite.org/index.html)
    - Reliable and powerful database as a service based on PostgreSQL.

#### Frameworks
1. [Bootstrap:](https://getbootstrap.com)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [JQuery Core:](https://code.jquery.com/)
    - JQuery library was implemented to use features within Materialize

#### Library
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

#### Programs
1. [Google Chrome:](https://www.google.co.uk/intl/en_uk/chrome/)
    - Default browser used to visually display the build process as well as utilising Chrome Dev Tools to assist where needed.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the code of the project after being pushed from GitPod.
1. [Visual Studio Code](https://code.visualstudio.com/)
    - Code editing software was used to replace GitPod as the free license expired due to over 50 hours useage. 
1. [GitHub Desktop:](https://desktop.github.com/)
    - A tool that allows you to interact with GitHub from the desktop
1. [Grammerly:](https://app.grammarly.com/)
    - Online tool which assists with the English grammar.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](#) during the design process.
1. [Stripe:](https://stripe.com/gb)
    - Online payment processing for internet businesses.
1. [Heroku:](https://www.heroku.com)
    - A platform as a service (PaaS) that enables me to deploy my website in the cloud.
1. [AWS:](https://aws.amazon.com/?nc2=h_lg)
    - Amazon Web Services (AWS) is a secure cloud services platform, allowing the running web and application servers in the cloud to host dynamic websites.

#### Other
1. [Django Secret Key Generator:](https://miniwebtool.com/django-secret-key-generator/)
    - The Django Secret Key Generator is used to generate a new SECRET_KEY that you can put in your settings.py module.
1. [Tempmail:](https://temp-mail.org/en/)
    - A free email service that allows to receive email at a temporary address that self-destructed after a certain time elapses
1. [JSON Formatter:](https://jsonformatter.org/)
    - A formatter which cleans JSON code to a more readable format
1. [Python Tutor:](http://pythontutor.com/)
    - A platform which helps a user to visualize python code.

## Testing

...

### Validation


On code completion, I ensured my code was validated with no snytax errors. I used [W3C Markup Validator](https://validator.w3.org/) for HTML5, [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) for CSS3 to ensure my code is W3C Compliant. I used [JSHint](https://jshint.com/) to helps to detect errors and potential problems in your JavaScript code. I also used [PEP8 Online](http://pep8online.com/) to validate my python scripts

#### Results

Page | Initial Errors | Resolved Errors | Error Notes
------------ | ------------- | ------------- | -------------
index.html| [Initial Errors](#) | [Resolved Errors](#) | ...

or use this template

#### HTML - [W3C Markup Validator](https://validator.w3.org/)

- 

#### CSS - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](#)

- 

#### JS - [JSHint](https://jshint.com/) - [Results](#)

- 

#### Python - [PEP8 Online](http://pep8online.com/) - [Results](#)

- 

### Further Testing

#### User Stories Testing from User Experience (UX) Section - [View Results](#)



#### Functionality and Usability Testing - [View Results](#)



#### Browser and Responsive Testing



### Known Issues

- 

## Deployment

### Making a Clone



### Making a Deployment



## Credits

### Content



### Code



### Media



### Acknowledgements

