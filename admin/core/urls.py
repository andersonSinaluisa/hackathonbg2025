from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProspectViewSet, ScoreHistoryViewSet, CreditApplicationViewSet

router = DefaultRouter()
router.register(r'prospects', ProspectViewSet)
router.register(r'score-history', ScoreHistoryViewSet)
router.register(r'credit-applications', CreditApplicationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
