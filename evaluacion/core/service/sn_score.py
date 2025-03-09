

from bs4 import BeautifulSoup
from linkedin_api import Linkedin
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

from core.model.redes_social import RedesSocial

class SocialScoreService:

    def get_data_by_dni(self, dni):
        '''
        user, following, followers, posts, likes, comments, shares, reactions, views, connections, social networks
        '''
        lista = RedesSocial.objects.filter(cedula=dni)

        
        return lista
    
    
    def calculate(self,identification):
        
        lista = self.get_data_by_dni(identification)
        
        total = 0

        total = len(lista)
        total_ontime = 0

        #calcula un score en base a la cantidad de seguidores, likes, comentarios, acciones, vistas, conexiones y redes sociales
        for item in lista:
           
            total_ontime += item.reputacion_en_redes
            if item.referencias_compras_largo_plazo:
                total_ontime += 1
            if item.interaccion_con_contenido_financiero:
                total_ontime += 1
            if item.presencia_articulos_lujo:
                total_ontime += 1
            if not item.frecuencia_publicaciones_ambientes_falsos:
                total_ontime += 1
            if item.aparicion_situaciones_riesgo:
                total_ontime += 1
            if item.nivel_edicion_fotos == 'Alto':
                total_ontime += 1
            if item.nivel_edicion_fotos == 'Medio':
                total_ontime += 0.5
            if item.nivel_edicion_fotos == 'Bajo':
                total_ontime += 0.2
            if any(x in item.categoria_gasto for x in ['Lujo', 'Tecnologia', 'Viajes']):
                total_ontime += 1

            
        
        #retorna el score de 0 a 1 en base a la cantidad de seguidores, likes, comentarios, acciones, vistas, conexiones y redes sociales
        if total == 0 or total_ontime == 0:
            return 0
        else:
            total_ontime = float(total_ontime)
            total = float(total)
            score = (total_ontime / total) * 0.0001
            return score