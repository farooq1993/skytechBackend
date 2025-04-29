from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('getAllServices/', views.GetallServices.as_view(), name='allServices'),
    path('itservice/', views.Itservices.as_view(), name='itservice'),
    path('getSingleRecord/<int:id>/', views.ServiceById.as_view(), name='singlerecord'),
    path('all_services/<int:id>/', views.SubserviceData.as_view(), name='all_services'), 
]