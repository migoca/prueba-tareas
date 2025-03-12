from rest_framework.routers import DefaultRouter
from .api.viewsets import FamiliaViewSet, TareaViewSet
from django.urls import path
from django.conf.urls import include

app_name = "tareas"

router = DefaultRouter()
router.register(r'familias', FamiliaViewSet, basename="familia")
router.register(r'tareas', TareaViewSet, basename="tarea")

urlpatterns = [
    path('', include(router.urls)),
]