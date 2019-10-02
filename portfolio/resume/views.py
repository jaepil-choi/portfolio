from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# import io
# from reportlab.pdfgen import canvas
from django.http import FileResponse

from .models import ResumePost

# Create your views here.

class ResumeView(ListView):
    model = ResumePost
    template_name = 'resume/home.html'

class ResumeDetail(DetailView):
    model = ResumePost
    template_name = 'resume/resume.html'