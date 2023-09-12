from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceptView.as_view(), name="accept"),
    path('list/',views.list,name="list"),
    path('list/<int:id>/',views.UserDetail, name="viewing"),
    path('resume/<int:resume_id>/',views.resume,name="resume"),
    
]
