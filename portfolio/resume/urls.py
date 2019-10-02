from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ResumeView.as_view(), name='list' ),
    path('<int:pk>', views.ResumeDetail.as_view(), name='detail'),
]
