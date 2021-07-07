from django.urls import path
from . import views

urlpatterns = [
    # Set of empty path to indicate this is the route URL, and its going to render views.index with the name Home.

    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]
