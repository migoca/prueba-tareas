from rest_framework import routers, serializers, viewsets
from ..models import Familia, Tarea
from .serializers import FamiliaSerializer, TareaSerializer
from rest_framework.filters import OrderingFilter


class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Familia.objects.all()  
    serializer_class = FamiliaSerializer

    def get_queryset(self):
        queryset = Familia.objects.all()
        nombre = self.request.query_params.get("nombre", None)
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)  # Búsqueda parcial        
        return queryset


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()    
    serializer_class = TareaSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['estado', 'fecha_vencimiento']

    def get_queryset(self):
        queryset = Tarea.objects.all()
        titulo = self.request.query_params.get("titulo", None)
        estado = self.request.query_params.get("estado", None)
        familia = self.request.query_params.get("familia", None)
        fecha_vencimiento = self.request.query_params.get("fecha_vencimiento", None)

        if titulo:
            queryset = queryset.filter(nombre__icontains=titulo)  # Búsqueda parcial
        if estado:
            queryset = queryset.filter(estado=estado)
        if familia:
            queryset = queryset.filter(familia=familia)
        if fecha_vencimiento:
            queryset = queryset.filter(fecha_vencimiento=fecha_vencimiento)
        return queryset
    