from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.accept, name="accept"),
    path('<int:id>/',views.resume,name="resume"),
    path('list/',views.list,name="list"),
]
