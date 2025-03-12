from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tarea, Familia


# Create your tests here.

class TareaAPITestCase(APITestCase):
    def setUp(self):
        self.familia = Familia.objects.create(nombre="Familia 1")

    
    def test_crear_tarea(self):        
        url = "/api/tareas/"
        data = {
            "titulo": "Tarea 1",
            "familia": self.familia.id,
            "descripcion": "Descripcion 1",
            "estado": "pendiente"
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarea.objects.count(), 1)
        self.assertEqual(Tarea.objects.first().titulo, "Tarea 1")

    
    def test_listar_tareas(self):        
        Tarea.objects.create(titulo="Tarea 1", familia=self.familia, descripcion="Descripcion 1")
        Tarea.objects.create(titulo="Tarea 2", familia=self.familia, descripcion="Descripcion 2")

        url = "/api/tareas/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Debe haber 2 tareas


    def test_actualizar_tarea(self):
        tarea = Tarea.objects.create(titulo="Tarea 1 viejo", familia=self.familia, descripcion="Descripcion 1")

        url = f"/api/tareas/{tarea.id}/"
        data = {"titulo": "Nuevo Titulo", "familia": self.familia.id, "descripcion": "Descripcion Nueva"}

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verificar que el nombre fue actualizado
        tarea.refresh_from_db()
        self.assertEqual(tarea.titulo, "Nuevo Titulo")

    
    def test_eliminar_tarea(self):
        """Verifica que se puede eliminar una tarea"""
        tarea = Tarea.objects.create(titulo="Tarea a eliminar", familia=self.familia)

        url = f"/api/tareas/{tarea.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tarea.objects.count(), 0)  # No deben quedar tareas
