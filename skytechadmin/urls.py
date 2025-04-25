from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('all_services/<int:id>/', views.SubserviceData.as_view(), name='all_services'), 
]