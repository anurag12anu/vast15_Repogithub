from django.urls import path,include

from . import views

urlpatterns=[
    
    
    path('student_list/',views.student_list,name='list'),
    path('student_create/',views.student_create,name='create_list'),
    
]
