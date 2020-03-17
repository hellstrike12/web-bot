import requests
import csv
from multiprocessing import Pool
from bs4 import BeautifulSoup

def minerar(index):
    fileName = page_list[index]
    url = page_list[index]

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
                        productBox = soup.find_all('div', {'class': 'product-box-price'})
                        link = soup.find_all('a',{'class': 'product-box-link is-lazyloaded image product-image-rotate'}, href=True)
                        precos = []

                        for x in range(len(productBox)-1):
                            for y in range(len(productBox[x].attrs['class'])): 
                                if (productBox[x].attrs['class'][y] == 'hide-mobile'): # Remover entrada bugada
                                    productBox.pop(x)
                                    break
                                
                        for x in range(len(productBox)-1):
                            for y in range(len(productBox[x].attrs['class'])):
                                if (productBox[x].attrs['class'][y] == 'is-special-price'): # Com desconto
                                    priceTo = productBox[x].contents[3].text
                                    precos.append(priceTo)
                                    break
                                
                                elif (len(productBox[x].attrs['class']) == 1): # Sem disconto
                                    priceFrom = productBox[x].contents[1].text
                                    precos.append(priceFrom)
                                    break

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
    indexes = range(len(page_list))
    p = Pool()
    p.map(minerar, indexes)
    p.close()
    p.join()