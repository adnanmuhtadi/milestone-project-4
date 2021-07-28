from django import template

# creating a variable called register
register = template.Library()


# filter decorator to register outour function
# as a template filter
@register.filter(name='calc_subtotal')
# function that takes a price and quantity as parameters
def calc_subtotal(price, quantity):
    return price * quantity
