from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('brandlist/', views.getbrand),
]

urlpatterns = format_suffix_patterns(urlpatterns)