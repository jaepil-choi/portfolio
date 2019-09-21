from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ResumeView.as_view(), name='list' ),
]
