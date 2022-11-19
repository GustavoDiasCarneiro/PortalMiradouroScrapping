from bs4 import BeautifulSoup
import requests


def datas():
    lista_de_datas = []
    dados_html = requests.get('http://www.portalmiradouro.com.br/site/category/portal').content
    site = BeautifulSoup(dados_html, 'html.parser')
    bloco_de_noticia = site.findAll('div', attrs={'class': 'blogmagazine-archive-post-content-wrapper'})

    for data_da_noticia in bloco_de_noticia:
        data_da_noticia = data_da_noticia.find('time').text
        lista_de_datas.append(data_da_noticia)
    return lista_de_datas
