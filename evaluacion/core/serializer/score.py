
from rest_framework import serializers
from core.model import Score


class SerializerScore(serializers.Serializer):
    identification = serializers.CharField(max_length=10)
    

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'