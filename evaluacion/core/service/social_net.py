from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4 as bs
import re
class SocialNetService:

    def run(self, ig_user):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self
        .options)
        
        self.driver.get('https://www.instagram.com/' + ig_user)
        self.driver.implicitly_wait(10)
        
        
        html = self.driver.page_source
        
        
        #limpiar con beautifulsoup
        #print(html)
        
        
        html = bs.BeautifulSoup(html, 'html.parser')
        description = html.find('meta', property='og:description')
        '''796 seguidores, 1,031 siguiendo, 61 publicaciones - Ver fotos y vídeos de Instagram de Danaé (@to_danaeee)'''

        if description:
            content = description['content']

            # Usar regex para extraer los números
            matches = re.findall(
                r'([\d,]+) (seguidores|siguiendo|publicaciones)', content)

            # Convertir los valores con comas a enteros
            data = {tipo: int(valor.replace(',', '')) for valor, tipo in matches}

            return data
        else:
            return None
        
        
    
    def calculate(self, ig_user):
        data = self.run(ig_user)
        if data:
            if data['seguidores'] > 1000:
                return 0.8
            elif data['seguidores'] > 500:
                return 0.5
            elif data['seguidores'] > 100:
                return 0.3
            else:
                return 0.1
        else:
            return 0.0