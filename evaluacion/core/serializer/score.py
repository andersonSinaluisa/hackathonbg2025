
from rest_framework import serializers
from core.model import Score


class SerializerScore(serializers.Serializer):
    identification = serializers.CharField(max_length=10)
    income_value = serializers.IntegerField()
    username_social = serializers.CharField(max_length=100)
    

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'