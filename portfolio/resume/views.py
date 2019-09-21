from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView

from .models import ResumePost

# Create your views here.

class ResumeView(ListView):
    model = ResumePost
    template_name = 'resume/home.html'