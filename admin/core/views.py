from rest_framework import viewsets
from .models.prospect import Prospect
from .models.score_history import ScoreHistory
from .models.credit_application import CreditApplication
from .serializers import ProspectSerializer, ScoreHistorySerializer, CreditApplicationSerializer

class ScoreHistoryViewSet(viewsets.ModelViewSet):
    queryset = ScoreHistory.objects.all()
    serializer_class = ScoreHistorySerializer

class ProspectViewSet(viewsets.ModelViewSet):
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer

class CreditApplicationViewSet(viewsets.ModelViewSet):
    queryset = CreditApplication.objects.all()
    serializer_class = CreditApplicationSerializer