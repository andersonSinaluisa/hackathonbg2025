from django.conf import settings
import requests
from rest_framework.response import Response

class ScoreBuroService:
    
    
    
    def calculate(self,identification):
        url = settings.API_BANCA + "/Hackathon/scoreburo?cedula=" + \
            identification + "&pageNumber=1&pageSize=1000"
            
            
        response = requests.get(url)
        
        if response.status_code == 200:

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
        