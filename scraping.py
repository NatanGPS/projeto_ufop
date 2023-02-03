from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import pandas as pd


informacoes_listas = []


'''
url = 'http://dados.ufop.br/dataset/graduacao-evadidos'
response = urlopen(url)
html = response.read()
html = html.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
'''
##last_page = int(soup.find('span', attrs={'class': 'info-pages'}).get_text().split()[-1])
for i in range(2):
    
    response = urlopen('http://dados.ufop.br/dataset/graduacao-evadidos')
    html = response.read()
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    
    
    
    
    infos_max = soup.find('div', attrs={'class': 'module-content'}).findAll('li', attrs={'class': 'resource-item'})
    for geral in infos_max:
        #dicionario geral
        informacoes_links = []
        informacoes = geral.find('a', attrs={'class': 'heading'}).findAll('href')
        informacoes_links.append(informacoes)
    print(informacoes_links)


        
