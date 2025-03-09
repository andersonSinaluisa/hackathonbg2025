from rest_framework import serializers
from core.model import Cnel

class CnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnel
        fields = '__all__'