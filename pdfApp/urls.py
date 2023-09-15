from django.urls import path
from . import views 

urlpatterns = [
    #/home/
    path('', views.acceptView.as_view(), name="accept"),
    #home/list/
    path('list/',views.list,name="list"),
    #/home/list/id
    path('list/<int:id>/',views.UserDetail, name="viewing"),
    #/home/resume/id
    path('resume/<int:resume_id>/',views.resume,name="resume"),
    #/home/update/id
    path('update/<int:id>/', views.update_form, name="update"),
    #home/delete/id
    path('delete/<int:id>/', views.delete_form, name="deleteform"),
    path('view_resume/<str:username>/', views.view_resume, name="view_resume"),
    
]
