import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'class': 'poly-card poly-card--list'})

if produtos:
    for produto in produtos:
        
        titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
        link = produto.find('a', attrs={'class': 'ui-search-link'})

        real = produto.find('span', attrs={'class': 'price-tag-fraction'})
        centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

        print(produto.prettify())
        if titulo:
            print('Título do produto:', titulo.text)
        if link:
            print('Link do produto:', link['href'])

        if (centavos):
            print('Preço do produto: R$', real.text + ',' + centavos.text)
        else:
            if real:
                print('Preço do produto: R$', real.text)
        
        print('\n\n')
        break
else:
    print("Sem produtos encontrados")