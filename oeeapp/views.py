
from rest_framework import generics
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer

class MachineListAPIView(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class ProductionLogListAPIView(generics.ListAPIView):
    serializer_class = ProductionLogSerializer

    def get_queryset(self):
        machine_name = self.request.query_params.get('machine_name', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        
        queryset = ProductionLog.objects.all()
        if machine_name:
            queryset = queryset.filter(machine__machine_name=machine_name)
        if start_date:
            queryset = queryset.filter(start_time__gte=start_date)
        if end_date:
            queryset = queryset.filter(end_time__lte=end_date)
        return queryset



