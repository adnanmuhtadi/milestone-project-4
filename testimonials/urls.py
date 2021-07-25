from django.urls import path
from . import views

urlpatterns = [
    # Set of empty path to indicate this is the route URL,
    # and its going to render views.index with the name Home.

    path('', views.all_testimonials, name='testimonials'),
    path('add/', views.add_testimonial, name='add_testimonial'),
    path('edit/<int:testimonial_id>/', views.edit_testimonial, name='edit_testimonial'),
    path('delete/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]
