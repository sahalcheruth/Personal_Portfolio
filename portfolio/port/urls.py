from django.urls import path
from .import views


urlpatterns = [
    path('',views.index_view,name='home'),
    path('skill/',views.skill_view,name='skill'),
    path('about/',views.about_view,name='about'),
    path('resume/',views.resume_view,name='resume'),
    path('contact/', views.contact_view, name='contact'),

    
]