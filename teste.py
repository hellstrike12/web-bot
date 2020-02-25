import requests
from lxml import html

# page = requests.get('https://br.advfn.com/indicadores/taxa-selic/valores-historicos')
# tree = html.fromstring(page.content)
# linha = 0
# contador = 2

# while linha < 219:

#     data = list(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[1]/text()' % contador))[0]
#     vigencia = list(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[2]/text()' % contador))[0]
#     taxa = list(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[3]/text()' % contador))[0]

#     inserir = data + ' ; ' + vigencia + ' ; ' + taxa
#     print(inserir)

#     linha = linha + 1
#     contador = contador + 1

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'} # 403 Forbidden
page = requests.get('https://br.investing.com/currencies/usd-brl-historical-data', headers=headers)
tree = html.fromstring(page.content)
linha = 0
contador = 1

while linha < 11:
    
    data = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[1]/text()' % contador))[0]
    ultimo = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[2]/text()' % contador))[0]
    abertura = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[3]/text()' % contador))[0]
    maxima = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[4]/text()' % contador))[0]
    minima = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[5]/text()' % contador))[0]
    var = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[6]/text()' % contador))[0]

    inserir = data + ' ; ' + ultimo + ' ; ' + abertura + ' ; ' + maxima + ' ; ' + minima + ' ; ' + var
    print(inserir)

    linha = linha + 1
    contador = contador + 1