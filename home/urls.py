from django.urls import path
# from .views import home_view, jai_shree_ram, create_user
from . import views
from .views import *

urlpatterns = [
    path('create/', create_user_order, name='create'),
    path('update/', update_order, name='update'),
    path('delete/<int:id>', delete_order, name='updating'),
    path('read-all-Orders/', read_all_orders, name='read_all_orders'),
    path('order/<int:id>', read_unique_order_id, name='reading_specific_id'),
    path('patch/', patch_krunga, name='patching')
]