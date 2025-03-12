from rest_framework import serializers
from ..models import Tarea, Familia


class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = '__all__'    

    def validate_nombre(self, value):
        if "casa" in value.lower():
            raise serializers.ValidationError("'casa' no está permitido en el nombre.")
        return value


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'    

    def validate_estado(self, value):
        if value not in [x[0] for x in Tarea.CHOICES_ESTADO]:
            raise serializers.ValidationError("Estado no permitido")
        return value
    
    def validate_titulo(self, value):
        if "casa" in value.lower():
            raise serializers.ValidationError("'casa' no está permitido en el nombre.")
        return value
    
    #familia, descripcion    
    



