from django.conf import settings
import requests
from rest_framework.response import Response

class ScoreBuroService:
    
    
    
    def calculate(self,identification):
        url = settings.API_BANCA + "/Hackathon/scoreburo?cedula=" + \
            identification + "&pageNumber=1&pageSize=1000"
            
            
        response = requests.get(url)
        
        if response.status_code == 200:
        
            '''{
                "scoreId": 1,
                "cedula": "5926995710",
                "score": 237,
                "probMorosidad": 30,
                "maximoCupoTC": 17074,
                "marcaTarjeta": "Discover",
                "cupoCreditos": 5859
              }'''
              
            data = response.json()
            
            score = data['score']
            probMorosidad = data['probMorosidad']
            maximoCupoTC = data['maximoCupoTC']
            marcaTarjeta = data['marcaTarjeta']
            cupoCreditos = data['cupoCreditos']
            
            
            return Response({
                'score': score,
                'probMorosidad': probMorosidad,
                'maximoCupoTC': maximoCupoTC,
                'marcaTarjeta': marcaTarjeta,
                'cupoCreditos': cupoCreditos
            })
            
            
            
            
