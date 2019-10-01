from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectView.as_view(), name='list' ),
    path('<int:pk>', views.ProjectDetail.as_view(), name='detail' ),
]
