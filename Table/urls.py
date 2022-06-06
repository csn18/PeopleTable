from django.urls import path
from Table.views import *

urlpatterns = [
    path('', table_page, name='table_page'),
    path('filter/name', filter_name, name='filter_name'),
    path('filter/age', filter_age, name='filter_age'),
    path('data/get', get_data, name='get_data'),
    path('search/name', search_by_name, name='search_by_name'),
    path('search/age', search_by_age, name='search_by_age'),
    path('get/data', get_data, name='get_data'),
]
