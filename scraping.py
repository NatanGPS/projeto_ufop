import requests
from bs4 import BeautifulSoup





class scrapping:
    def __init__(self):
        self.url = 'http://dados.ufop.br/dataset/graduacao-evadidos'
        self.response = requests.get(self.url)
        self.site  = BeautifulSoup(self.response.text, 'html.parser')
        self.links = self.site.find('div', attrs = {'class': 'module-content'})
        self.urls_para_baixar = []
        self.lista = []

    def Iniciar(self):
        self.achar_links()
        self.entrar_links()
# Acha os links  e os adiciona em uma lista 
    def achar_links(self):
        for self.link in self.links.find_all('a', attrs = {'class': 'heading'}):
            self.achar_link = self.link.get('href')
            # esses ifs aninhados servem para filtrar alguns links que nao quero
            if self.achar_link != '#':
                if 'mailto:' not in self.achar_link:
                    self.lista.append(self.achar_link)
        
       

    # Essa função vai entrar
    def entrar_links(self):
        for entrando in self.lista:
            self.url2 = entrando

            self.response2 = requests.get('http://dados.ufop.br'+ self.url2)
            self.site2 = BeautifulSoup(self.response2.text, 'html.parser')
            self.arquivoscsv = self.site.find('div', attrs = {'class': 'module-content'})
            
        for self.cada_um in self.arquivoscsv.find_all('a'):
            self.pegar_link = self.cada_um.get('href')
            if self.pegar_link != '#':
                if 'mailto:' not in self.pegar_link:  
                    self.urls_para_baixar.append(self.pegar_link)

        print(self.urls_para_baixar)





comecar = scrapping()
comecar.Iniciar()