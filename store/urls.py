from django.urls import path
from . import views


url_patterns=[
    path('', views.store_page, name='store'),
    path('category/<slug:category_slug>/', views.store_page, name='product_by_category')
]