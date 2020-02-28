import requests
import csv
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

head = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept-Ranges": "bytes",
    "Age":"0",
    "Cache-Control": "no-store, no-cache, must-revalidate",
    "Connection":"keep-alive",
    "Content-Encoding":"gzip",
    "Content-Length": "1927",
    "Content-Security-Policy":"upgrade-insecure-requests; block-all-mixed-content",
    "Content-Type":"text/html; charset=UTF-8",
    "Date":"Thu, 27 Feb 2020 20:41:12 GMT",
    "Expires":"Thu, 19 Nov 1981 08:52:00 GMT",
    "Pragma":"no-cache",
    "Server":"nginx/1.16.1",
    "Set-Cookie":"ses_id=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/; domain=br.investing.com",
    "Vary":"Accept-Encoding,User-Agent",
    "Via":"1.1 varnish",
    "X-Powered-By":"PHP/7.1.8",
    "X-Varnish":"187149423"
}
data = {
    "curr_id":"2103",
    "smlID":"107254",
    "header":"USD/BRL+Dados+Históricos",
    "st_date":"01/01/2000",
    "end_date":"01/01/2020",
    "interval_sec":"Daily",
    "sort_col":"date",
    "sort_ord":"ASC",
    "action":"historical_data"
}

page = requests.get('https://br.investing.com/currencies/usd-brl-historical-data', headers=headers)
post = requests.post('https://br.investing.com/instruments/HistoricalDataAjax', data=data, headers=head)
print(page)
print(post)
tree = html.fromstring(page.content)
linha = 0
contador = 1

with open('banco.csv', 'w', newline='') as csvfile:
    fieldnames = ['Data', 'Último', 'Abertura', 'Máxima', 'Mínima', 'Variação']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()

    while linha < 7305:
        
        data = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[1]/text()' % contador))[0]
        ultimo = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[2]/text()' % contador))[0]
        abertura = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[3]/text()' % contador))[0]
        maxima = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[4]/text()' % contador))[0]
        minima = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[5]/text()' % contador))[0]
        var = list(tree.xpath('//*[@id="results_box"]/table/tbody/tr[%d]/td[6]/text()' % contador))[0]

        # inserir = data + ' ; ' + ultimo + ' ; ' + abertura + ' ; ' + maxima + ' ; ' + minima + ' ; ' + var
        spamwriter.writerow({'Data': data, 'Último': ultimo, 'Abertura': abertura,'Máxima': maxima, 'Mínima': minima, 'Variação': var})
        
        linha = linha + 1
        contador = contador + 1