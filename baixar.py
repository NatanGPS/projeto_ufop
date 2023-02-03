import requests
import os


def baixar_arquivo(url, endereco ):
        #Faz uma requisição ao servidor
        resposta = requests.get(url)
        if resposta.status_code == requests.codes.OK:   
            with open(endereco, 'wb') as arquivo:
                arquivo.write(resposta.content)
            print(f"Dowload feito com sucesso. salvo em {endereco}")
        else:
            resposta.raise_for_status()

n = int(input("Quantos arquivos deseja baixar?"))
links = []
#3 for usado para adicionar as urls em um lista
for i in range (1, n + 1):
    link = input(f"Digite  o link {i}: ")
    links.append(link)
print(links)
# Cria um diretorio de saida 
OUTPUT_DIR = "arquivos"
index = 0    
for j in range(n +1):
    nome_arquivo = os.path.join(OUTPUT_DIR, f'arquivo{j}.csv')
    baixar_arquivo(links[index], nome_arquivo)
    index +=1

    #PAREI NA TENTATIVA DE FAZER O SCRAPING DAS URLS PARA ADIOCIONAR NAS LISTAS E BAIXAR TODOS OS ARQUIVOS NECESSARIOS