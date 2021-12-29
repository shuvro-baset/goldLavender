from django.urls import path
from django.views.generic import TemplateView
from mobileApp.views import home, add_mobile, mobile_list, delete_mobile, delete_mobiles, search_mobile_list

urlpatterns = [
    path('home/', home, name='home'),
    path('add-mobile/', add_mobile, name='add-mobile'),
    path('mobile-list/', mobile_list, name='mobile-list'),
    path('search-mobile/', search_mobile_list, name='search-mobile'),
    path('delete/<int:id>', delete_mobile, name='delete'),
    path('delete/', delete_mobiles, name='delete-mobiles'),

]
