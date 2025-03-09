from rest_framework.views import APIView
from rest_framework.response import Response

from core.service.calculate_score import CalculateScoreService
from core.serializer.score import ScoreSerializer, SerializerScore
from core.service.social_net import SocialNetService


class CalculateScore(APIView):
    
    serializer_class = SerializerScore
    
    
    def __init__(self, **kwargs):
        self.service = CalculateScoreService()
    
    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data = self.service.calculate(**data.validated_data)
        return Response(data)



class InstagramInfo(APIView):
    
    def __init__(self, **kwargs):
        self.service = SocialNetService()
    
    def get(self, request):
        ig_user = request.query_params.get('ig_user')
        if not ig_user:
            return Response({'error': 'ig_user is required'}, status=400)
        data = self.service.run(ig_user)
        return Response(data)