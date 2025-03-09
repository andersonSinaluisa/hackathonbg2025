


from evaluacion.core.service.score_buro import ScoreBuroService
from rest_framework.response import Response

class CalculateScoreService:
    
    def __init__(self):
        self.score_buro = ScoreBuroService()

    def calculate(self, identification):
        score_buro = self.score_buro.calculate(identification)
        score_buro_points = score_buro['score']
        
        return Response({
            'score':  score_buro_points,
        })
        
        
        