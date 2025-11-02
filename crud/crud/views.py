from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = "home.html"
    
