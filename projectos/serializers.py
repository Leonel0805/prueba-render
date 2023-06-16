#importamos serializer desde rest_framework 
#seria casi como los forms solo que para serializar
#e indicamos que esta basado en un modelo que ya creamos de models, como los forms
from rest_framework import serializers
from .models import Projecto

class ProjectoSerializacion(serializers.ModelSerializer):
    class Meta:
        model = Projecto
        fields = ['id', 'titulo', 'descripcion', 'tecnologia', 'fecha_creado']
        
        #le indicamos que campo es solo lectura, y no puede ser actualizado ni modificado
        read_only_fields = ['fecha_creado']