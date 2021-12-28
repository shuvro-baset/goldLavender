from django.urls import path
from django.views.generic import TemplateView
from mobileApp.views import Home, MobileList

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('mobile-list/', MobileList.as_view(), name='mobile-list'),

]
