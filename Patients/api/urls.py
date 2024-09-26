from django.urls import path 
from . import views

urlpatterns = [
    path("patients/", views.PatientListCreate.as_view(), name= "patient_view_create"), 
    path("patients/<int:pk>/", views.PatientRetrieveUpdateDestroy.as_view(), name= "update")
]