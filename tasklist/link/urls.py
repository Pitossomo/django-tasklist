from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path('create-category/', views.create_category, name='create_category'),
    path('create-link/', views.create_link, name='create_link'),
    path('links/', views.links, name='links'),
    path('categories/', views.categories, name='categories'),
]
