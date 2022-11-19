from bs4 import BeautifulSoup
from noticia.links import links
import requests


def imagens():
    lista_de_imagens = []
    for x in range(10):
        dados_html = requests.get(links()[x]).content
        site = BeautifulSoup(dados_html, 'html.parser')
        bloco_de_noticia = site.findAll('div', attrs={'class': 'entry-content'})
        for link_da_noticia in bloco_de_noticia:
            lista_de_imagens.append([])
            for link in link_da_noticia.find_all('a', href=True):
                link = link['href']
                lista_de_imagens[x].append(link)

    return lista_de_imagens
