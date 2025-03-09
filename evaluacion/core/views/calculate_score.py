from rest_framework.views import APIView
from rest_framework.response import Response

from core.service.calculate_score import CalculateScoreService
from core.serializer.score import ScoreSerializer, SerializerScore


class CalculateScore(APIView):
    
    serializer_class = SerializerScore
    
    
    def __init__(self, **kwargs):
        self.service = CalculateScoreService()
    
    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        score = 0
        self.service.calculate(data.validated_data)
        return Response({'score': score})