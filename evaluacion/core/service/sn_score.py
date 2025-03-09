

from bs4 import BeautifulSoup
from linkedin_api import Linkedin
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

class SocialScoreService:

    def get_data_by_dni(self, dni):
        '''
        user, following, followers, posts, likes, comments, shares, reactions, views, connections, social networks
        '''
        lista = []
        
        for _ in range(0, random.randint(0, 5)):

            data = {
                'user': 'user',
                'following': random.randint(0, 1000),
                'followers': random.randint(0, 1000),
                'posts': random.randint(0, 1000),
                'likes': random.randint(0, 1000),
                'comments': random.randint(0, 1000),
                'shares': random.randint(0, 1000),
                'reactions': random.randint(0, 1000),
                'views': random.randint(0, 1000),
                'connections': random.randint(0, 1000),
                'social_networks': random.randint(0, 1000),
            }
            lista.append(data)
        
        return lista
    
    
    def calculate(self,identification):
        
        lista = self.get_data_by_dni(identification)
        
        total = 0

        total = len(lista)
        total_ontime = 0
        #calcula un score en base a la cantidad de seguidores, likes, comentarios, acciones, vistas, conexiones y redes sociales
        for item in lista:
            total_ontime += item['followers'] + item['likes'] + item['comments'] + item['shares'] + item['reactions'] + item['views'] + item['connections'] + item['social_networks']
            
        
        #retorna el score de 0 a 1 en base a la cantidad de seguidores, likes, comentarios, acciones, vistas, conexiones y redes sociales
        score = total_ontime / total
        return score