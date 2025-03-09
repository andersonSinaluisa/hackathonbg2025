from django.conf import settings
import requests
from core.repository.cnel_repository import RepositoryCNEL


class CnelApiService:

    def __init__(self, repository: RepositoryCNEL):
        self.repository = repository

    def get_data_by_dni(self, dni):
        url = "/" + settings.CNEL_API_URL + dni+"/CEDULA_RUC"
        response = requests.get(url)

        try:
            if response.status_code == 200:

                data = response.json()

                self.repository.create(data['data'])
            else:
                raise ValueError(
                    "Error al obtener los datos del servicios basicos")

        except Exception as e:
            raise ValueError(
                "Error al obtener los datos del servicios basicos")

    
    
    def calculate(self, dni):
        