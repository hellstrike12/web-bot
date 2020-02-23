import requests
import csv
from server import executar
from bs4 import BeautifulSoup

num_pag = 1 # Contador de páginas

# CSV
with open('teste.csv', 'w', newline='') as csvfile: # Criar arquivo csv
    fieldnames=['Marca', 'Modelo', 'Preço', 'Link'] # Nomes das colunas
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()

    while (num_pag <= 2):
        contador = 0 # Resetar contador
        print('Página ' + str(num_pag)) # Debug
        page = requests.get("https://www.dafiti.com.br/roupas-masculinas/?page={}".format(num_pag)) # Mudar pagina
        soup = BeautifulSoup(page.content,'html.parser') # Abrir pagina com bs4

        # Encontrar todos os elementos HTML por tag e classe
        marca = soup.find_all('div',{'class': 'product-box-brand'}) 
        modelo = soup.find_all('p',{'class' : 'product-box-title hide-mobile'})
        preco = soup.find_all('span',{'class': 'product-box-price-from'})
        link = soup.find_all('a',{'class': 'product-box-link is-lazyloaded image product-image-rotate'}, href=True)

        while (contador <= (len(marca) - 1)):
            # Inserir dados no arquivo CSV
            spamwriter.writerow({'Marca': marca[contador].text, 'Modelo': modelo[contador].text, 'Preço': preco[contador].text, 'Link': link[contador]["href"]})

            contador += 1

        num_pag += 1 # Mudar de pagina