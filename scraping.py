import requests
from bs4 import BeautifulSoup
import os




class scrapping:
    def __init__(self):
        
        self.grupos = []
        self.urls_para_baixar = []
        self.lista = []
        self.lista_inicial = []
        self.OUTPUT_DIR = "output"
        self.index = 0
    
    def Iniciar(self):
        self.secao_por_secao()
        self.procurando_todos_conjuntos()
        self.achar_links()
        self.entrar_links()
        self.filtrar_links()
        
    # Pega cada seção da pagina inicial do site dados.ufop e pega os links de cada grupo de dados
    def secao_por_secao(self):
        url = 'http://dados.ufop.br'
        response = requests.get(url)
        site  = BeautifulSoup(response.text, 'html.parser')
        links = site.find('div', attrs = {'class': 'hero'})
        
        for link in links.find_all('a', attrs={'class': 'media-view'}):
            achar_urls = link.get('href')
            
            if achar_urls != '#':
                if 'http://dados.ufop.br' not in achar_urls:
                    self.grupos.append('http://dados.ufop.br' + achar_urls)
                else:
                    self.grupos.append(achar_urls)  
    

    
    #Essa funcao é responsavel por pegar os links de todos os conjuntos de uma determinada seção
    def procurando_todos_conjuntos(self):
        for procurar_todos_grupos in self.grupos:
            url = procurar_todos_grupos
            response1 = requests.get(url)
            site1  = BeautifulSoup(response1.text, 'html.parser')
            links1 = site1.find_all('h3', attrs = {'class': 'dataset-heading'})
            
            for conjunto in links1:
                buscando1 = conjunto.find('a')
                buscando_link = buscando1.get('href')
                
                if 'dataset' in buscando_link:
                    if 'mailto:' not in buscando_link:
                        if buscando_link != '#':
                            if 'http://dados.ufop.br' not in buscando_link:
                                self.lista_inicial.append('http://dados.ufop.br' + buscando_link)
                            else:
                                self.lista_inicial.append(buscando_link)

# Acha os links  e os adiciona em uma lista 
    def achar_links(self):
        for o in self.lista_inicial:
            self.url = o
            self.response = requests.get(self.url)
            self.site  = BeautifulSoup(self.response.text, 'html.parser')
            self.links = self.site.find('div', attrs = {'class': 'module-content'})
            
            for self.link in self.links.find_all('a', attrs = {'class': 'heading'}):
                self.achar_link = self.link.get('href')
                # esses ifs aninhados servem para filtrar alguns links que nao quero
                if self.achar_link != '#':
                    if 'mailto:' not in self.achar_link:
                        if 'dataset' in self.achar_link:
                            self.lista.append(self.achar_link)
    # Essa função vai entrar nos links obtidos pela lista self.lista e vai obter novos links para adicionalos em outros self.urls_para_baixar
    def entrar_links(self):
        for entrando in self.lista:
            self.url2 = entrando
            
            self.response2 = requests.get('http://dados.ufop.br'+ self.url2)
            self.site2 = BeautifulSoup(self.response2.text, 'html.parser')
            self.arquivoscsv = self.site2.find('div', attrs = {'class': 'module-content'})

            for links in self.arquivoscsv.find_all('a'):
                self.pegar_link = links.get('href')
                if self.pegar_link != '#':
                    if 'mailto:' not in self.pegar_link:  
                        if '.csv' in self.pegar_link:
                            self.urls_para_baixar.append(self.pegar_link)
   
   # Filtra os links e chama a funcao baixar_links
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