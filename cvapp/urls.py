from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('resumeTemplate/', views.acceptView.as_view(), name="accept"),
]
