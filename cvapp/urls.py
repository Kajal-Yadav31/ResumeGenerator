from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),

    path('resumeTemplate/', views.acceptView.as_view(), name="accept"),

    path('list/', views.list, name="list"),

    path('list/<int:id>/', views.UserDetail, name="viewing"),

    path('resume/<int:resume_id>/', views.resume, name="resume"),

    path('update/<int:id>/', views.update_form, name="update"),

    path('delete/<int:id>/', views.delete_form, name="deleteform"),

]
