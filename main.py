import requests
import csv
import multiprocessing
from bs4 import BeautifulSoup

def minerar(fileName, url):
    print("Starting process...")
    num_pag = 1 # Contador de páginas
    # CSV
    with open('csv/' + fileName + '.csv', 'w', newline='') as csvfile: # Criar arquivo csv
        fieldnames=['Marca', 'Modelo', 'Preço', 'Link'] # Nomes das colunas
        spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        spamwriter.writeheader()

        while True:
            page = requests.get("https://www.dafiti.com.br/{0}/?page={1}".format(url, num_pag)) # Mudar pagina
            soup = BeautifulSoup(page.content,'html.parser') # Abrir pagina com bs4

            try:
                pageNotFound = soup.find_all('div', {'class':'catalog-no-results-page'})
                print(pageNotFound[0])
                break
            except IndexError: # Pagina existe
                while True:
                    try:
                        contador = 0 # Resetar contador

                        # Encontrar todos os elementos HTML por tag e classe
                        marca = soup.find_all('div',{'class': 'product-box-brand'}) 
                        modelo = soup.find_all('p',{'class' : 'product-box-title hide-mobile'})
                        preco = soup.find_all('span',{'class': 'product-box-price-from'})
                        link = soup.find_all('a',{'class': 'product-box-link is-lazyloaded image product-image-rotate'}, href=True)

                        while (contador <= (len(marca) - 1)):
                            # Inserir dados no arquivo CSV
                            spamwriter.writerow({'Marca': marca[contador].text, 'Modelo': modelo[contador].text, 'Preço': preco[contador].text, 'Link': link[contador]["href"]})
                            contador += 1

                    except IndexError: # Se não houver mais produtos, mudar para o proximo departamento
                        num_pag += 1 # Mudar de pagina
                        break
    
    print("Stopping...")

page_list = ["calcados-masculinos",
"roupas-masculinas", 
"bolsas-e-acessorios-masculinos", 
"esporte-masculino", 
"beleza-masc",
"calcados-femininos",
"roupas-femininas",
"bolsas-e-acessorios-femininos",
"esporte-feminino",
"beleza-fem"] # Lista de departamentos da loja

if __name__ == '__main__':
    jobs = []
    for i in range(4):
        p = multiprocessing.Process(target=minerar, args=(page_list[i], page_list[i],))
        jobs.append(p)
        p.start()