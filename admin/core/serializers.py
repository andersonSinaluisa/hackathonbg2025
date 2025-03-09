from rest_framework import serializers
from django.db import transaction
from .models.prospect import Prospect
from .models.score_history import ScoreHistory
from .models.credit_application import CreditApplication
from .models.financial_information import FinancialInformation

# 🔹 Serializer para ScoreHistory
class ScoreHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreHistory
        fields = '__all__'

# 🔹 Serializer para CreditApplication
class CreditApplicationSerializer(serializers.ModelSerializer):
    prospect_id = serializers.PrimaryKeyRelatedField(
        queryset=Prospect.objects.all(), source="prospect", required=False
    )
    monto_solicitado = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    plazo = serializers.IntegerField(required=False)
    estado = serializers.CharField(required=False) 

    class Meta:
        model = CreditApplication
        fields = ["id", "prospect_id", "monto_solicitado", "plazo", "fecha", "estado", "created_at", "updated_at"]

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
        
# 🔹 Serializer para Prospect
class ProspectSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(write_only=True, required=False) 

    class Meta:
        model = Prospect
        fields = '__all__'

    def create(self, validated_data):
        score_value = validated_data.pop('score', None) 
        cedula = validated_data["cedula"] 

        with transaction.atomic():
            prospect = Prospect.objects.create(**validated_data)

            if score_value is not None:
                score_instance = ScoreHistory.objects.create(score=score_value, user_id=prospect.cedula)
                prospect.score = score_instance
                prospect.save()

        return prospect

    def update(self, instance, validated_data):
        score_value = validated_data.pop('score', None)

        with transaction.atomic():
            # Actualizar campos del Prospect
            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            if score_value is not None:
                score_instance, _ = ScoreHistory.objects.get_or_create(score=score_value, user_id=instance.cedula)
                instance.score = score_instance  

            instance.save()
        return instance

    def delete(self, instance):
        with transaction.atomic():
            CreditApplication.objects.filter(prospect=instance).delete()
            ScoreHistory.objects.filter(user_id=instance.cedula).delete()
            instance.delete()
        return instance
    
class FinancialInformationSerializer(serializers.ModelSerializer):
    prospect_id = serializers.PrimaryKeyRelatedField(
        queryset=Prospect.objects.all(), source="prospect"
    )

    class Meta:
        model = FinancialInformation
        fields = '__all__'

    def create(self, validated_data):
        with transaction.atomic():
            informacion_financiera = FinancialInformation.objects.create(**validated_data)
        return informacion_financiera

    def update(self, instance, validated_data):
        with transaction.atomic():
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
        return instance

    def delete(self, instance):
        with transaction.atomic():
            instance.delete()
        return instance