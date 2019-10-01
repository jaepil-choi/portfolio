from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ProjectPost

# Create your views here.

class ProjectView(ListView):
    model = ProjectPost

class ProjectDetail(DetailView):
    model = ProjectPost