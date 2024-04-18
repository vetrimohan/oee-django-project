from django.urls import path
from . import views

urlpatterns = [
    path('machines/', views.MachineListAPIView.as_view(), name='machine-list'),
    path('production-logs/', views.ProductionLogListAPIView.as_view(), name='production-log-list'),
]
