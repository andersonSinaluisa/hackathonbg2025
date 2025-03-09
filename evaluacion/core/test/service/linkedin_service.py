from django.test import TestCase
from core.service.social_net import SocialNetService



class TestLinkedinService(TestCase):
    
    def test_get_score(self):
        linkedin_service = SocialNetService()
        linkedin_service.run()