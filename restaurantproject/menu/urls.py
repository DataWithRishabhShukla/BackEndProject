from django.urls import path 
from . import views 


app_name = 'menu'

urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.menu_list , name = 'menu_items'),
    path('about/',views.about,name='about'),
    path('item/<int:item_id>/',views.item_details,name='item_detail'),
    path('api/',views.menu_json,name='menu_json'),
    
]