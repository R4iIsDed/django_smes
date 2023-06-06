from rest_framework import serializers
from .models import Comuna

class comunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id_com','nombre','region']

