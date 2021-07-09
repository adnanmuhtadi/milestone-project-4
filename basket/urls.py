from django.urls import path
from . import views

urlpatterns = [
    # this is the route URL or the page we are creating

    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove/<item_id>/', views.remove_from_basket, name='remove_from_basket'),

]
