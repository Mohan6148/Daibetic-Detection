





from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('detection/', views.predicator, name='detection'),
    path('result',views.formInfo,name='result'),

    path('feedback/', views.feedback, name='feedback'),
]
