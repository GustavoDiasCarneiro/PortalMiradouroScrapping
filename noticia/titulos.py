from bs4 import BeautifulSoup
import requests


def titulos():
    lista_de_titulos = []
    dados_html = requests.get('http://www.portalmiradouro.com.br/site/category/portal').content
    # Converte o html em texto
    site = BeautifulSoup(dados_html, 'html.parser')
    # Encontra o título da notícia
    card = site.findAll('div', attrs={'class': 'blogmagazine-archive-post-content-wrapper'})
    for titulo in card:
        titulo = titulo.find('h2', attrs={'class': 'entry-title'}).text
        lista_de_titulos.append(titulo)
    return lista_de_titulos
