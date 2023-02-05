import requests
from bs4 import BeautifulSoup
import os




class scrapping:
    def __init__(self):
        self.url = 'http://dados.ufop.br/dataset/graduacao-evadidos'
        self.response = requests.get(self.url)
        self.site  = BeautifulSoup(self.response.text, 'html.parser')
        self.links = self.site.find('div', attrs = {'class': 'module-content'})
        self.urls_para_baixar = []
        self.lista = []
        self.lista_final = []
        self.OUTPUT_DIR = "output"
        self.index = 0
    
    def Iniciar(self):
        self.achar_links()
        self.entrar_links()
        #self.arquivo()
        self.filtrar_links()
        
        


# Acha os links  e os adiciona em uma lista 
    def achar_links(self):
        for self.link in self.links.find_all('a', attrs = {'class': 'heading'}):
            self.achar_link = self.link.get('href')
            # esses ifs aninhados servem para filtrar alguns links que nao quero
            if self.achar_link != '#':
                if 'mailto:' not in self.achar_link:
                    self.lista.append(self.achar_link)
        
       

    # Essa função vai entrar nos links obtidos pela lista self.lista e vai obter novos links para adicionalos em outros self.urls_para_baixar
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
                    if '.csv' in self.pegar_link:
                        self.urls_para_baixar.append(self.pegar_link)

    #def arquivo(self):
        #for j in range(len(self.urls_para_baixar)):
            #self.nome_arquivo = os.path.join(self.OUTPUT_DIR, f'arquivo{self.index}.csv')
            #self.index += 1
    
    def filtrar_links(self):
        for self.formata_isso_pfv in self.urls_para_baixar:
            if "http://dados.ufop.br" not in self.formata_isso_pfv:
               urls = ('http://dados.ufop.br'+ self.formata_isso_pfv)
            
            else:
                urls = self.formata_isso_pfv
            nome_arquivo = os.path.join(self.OUTPUT_DIR, f'arquivo{self.index}.csv')
            self.index += 1
            self.baixar_arquivo(urls, nome_arquivo)
            
# Essa funcao vai baixar os arquivos a partiir das urls da lista self.urls_para_baixar     
    
    def baixar_arquivo(self, url, endereco ):
        
        #Faz uma requisição ao servidor
        resposta = requests.get(url)
        if resposta.status_code == requests.codes.OK:   
            with open(endereco, 'wb') as arquivo:
                arquivo.write(resposta.content)
            print(f"Dowload feito com sucesso. salvo em {endereco}")
        else:
            resposta.raise_for_status()

comecar = scrapping()
comecar.Iniciar()