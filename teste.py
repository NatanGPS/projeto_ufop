import requests
from bs4 import BeautifulSoup
import os
import baixar




class scrapping:
    def __init__(self):
        self.url = 'http://dados.ufop.br/dataset/graduacao-evadidos'
        self.response = requests.get(self.url)
        self.site  = BeautifulSoup(self.response.text, 'html.parser')
        self.links = self.site.find('div', attrs = {'class': 'module-content'})
        self.urls_para_baixar = []
        self.lista = []
        self.lista_final = []
        self.OUTPUT_DIR = "arquivos"
        self.index = 0
    
    def Iniciar(self):
        self.achar_links()
        self.entrar_links()
        

# Acha os links  e os adiciona em uma lista 
    def achar_links(self):
        for self.link in self.links.find_all('a'):
            self.achar_link = self.link.get('href')
            
            # esses ifs aninhados servem para filtrar alguns links que nao quero
            if self.achar_link != '#':
                if 'mailto:' not in self.achar_link:
                    self.lista.append(self.achar_link)

    # Essa função vai entrar nos sites e buscar os links de downloads
    def entrar_links(self):
        for entrando in self.lista:
            self.url2 = entrando
            # faço um tratamento das urls para tornar elas funcionais
            if "http://dados.ufop.br" not in entrando:
                self.response2 = requests.get('http://dados.ufop.br'+ self.url2)
            
            else:
                self.response2 = requests.get(self.url2)
            
            self.site2 = BeautifulSoup(self.response2.text, 'html.parser')
            self.arquivoscsv = self.site.find('div', attrs = {'class': 'module-content'})
            
            for i in self.arquivoscsv.find_all('p'):
                self.pegar_link = i.get('href')
                # faço outro tratamento
                if '/dataset' in self.pegar_link:
                    self.urls_para_baixar.append(self.pegar_link)
        
        


    def formatar_urls_e_baixar(self):
        for j in self.urls_para_baixar:
            if "http://dados.ufop.br" not in j:
               self.arrumado = self.lista_final.append('http://dados.ufop.br'+ j)
        
            else:
                self.arrumado = self.lista_final.append(j)

            self.nome_arquivo = os.path.join(self.OUTPUT_DIR, f'arquivo{self.index}.csv')
            baixar.baixar_arquivo(self.arrumado, self.nome_arquivo)
            self.index += 1






comecar = scrapping()
comecar.Iniciar()