from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
