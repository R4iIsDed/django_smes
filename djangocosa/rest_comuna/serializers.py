from rest_framework import serializers
from menu.models import Comuna

class comunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id_com','nombre','region']

