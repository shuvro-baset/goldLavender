from django.shortcuts import render
from django.views import generic


# Create your views here.
class Home(generic.TemplateView):
    template_name = 'home.html'

    # def get(self):

class MobileList(generic.TemplateView):
    template_name = 'mobile-list.html'
