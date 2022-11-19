from bs4 import BeautifulSoup
import requests

lista_de_links = []


def links():
    global link
    dados_html = requests.get('http://www.portalmiradouro.com.br/site/category/portal').content

    site = BeautifulSoup(dados_html, 'html.parser')

    bloco_de_noticia = site.findAll('div', attrs={'class': 'blogmagazine-archive-post-content-wrapper'})

    for link_da_noticia in bloco_de_noticia:
        for link in link_da_noticia.find_all('a', href=True):
            link = link['href']
        lista_de_links.append(link)
    return lista_de_links
