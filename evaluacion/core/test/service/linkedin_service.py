from django.test import TestCase
from evaluacion.core.service.sn_score import LinkedInScore



class TestLinkedinService(TestCase):
    
    def test_get_score(self):
        linkedin_service = LinkedInScore()
        score = linkedin_service.get_score()
        self.assertEqual(score, 100)