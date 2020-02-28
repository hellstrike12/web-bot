import requests
import csv
from lxml import html

head = {
    "Host": "br.investing.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "181",
    "Origin": "https://br.investing.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://br.investing.com/currencies/usd-brl-historical-data",
    "Cookie": "PHPSESSID=c3lf9tjlj09n61ls3oiapvkf5o; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%222103%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A32%3A%22D%C3%B3lar+Americano+Real+Brasileiro%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Fusd-brl%22%3B%7D%7D%7D%7D; geoC=BR; prebid_page=0; prebid_session=0; adBlockerNewUserDomains=1582907313; gtmFired=OK; nyxDorf=ZGA0b2M8YiBhPjk1ZSg0PzZgNHFkYTcxYmY%3D; StickySession=id.9776037282.227.br.investing.com; adbBLk=30; G_ENABLED_IDPS=google; r_p_s_n=1"
}
data = {
    "curr_id":"2103",
    "smlID":"107254",
    "header":"USD/BRL+Dados+Históricos",
    "st_date":"01/01/1993",
    "end_date":"28/02/2020",
    "interval_sec":"Daily",
    "sort_col":"date",
    "sort_ord":"ASC",
    "action":"historical_data"
}

page = requests.post('https://br.investing.com/instruments/HistoricalDataAjax', headers=head, data=data)
tree = html.fromstring(page.content)

linha = 0
contador = 1

with open('banco.csv', 'w', newline='') as csvfile:
    fieldnames = ['Data', 'Último', 'Abertura', 'Máxima', 'Mínima', 'Variação']
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()

    while True:
        try:
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
        except IndexError: # Se não houver mais dados para minerar
            break
            
