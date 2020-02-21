import requests
import csv
from bs4 import BeautifulSoup

num_pag = 1

# CSV
with open('dafiti.csv', 'w', newline='') as csvfile:
    fieldnames=['Marca', 'Modelo', 'Preço', 'Link']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()

    while (num_pag <= 855):
        contador = 0
        print('Página ' + str(num_pag))
        page = requests.get("https://www.dafiti.com.br/roupas-masculinas/?page={}".format(num_pag))
        soup = BeautifulSoup(page.content,'html.parser')

        marca = soup.find_all('div',{'class': 'product-box-brand'})
        modelo = soup.find_all('p',{'class' : 'product-box-title hide-mobile'})
        preco = soup.find_all('span',{'class': 'product-box-price-from'})
        link = soup.find_all('a',{'class': 'product-box-link is-lazyloaded image product-image-rotate'}, href=True)

        while (contador <= (len(marca) - 1)):
            spamwriter.writerow({'Marca': marca[contador].text, 'Modelo': modelo[contador].text, 'Preço': preco[contador].text, 'Link': link[contador]["href"]})
            contador += 1

        num_pag += 1