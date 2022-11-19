from bs4 import BeautifulSoup
import requests


def anuncios():
    lista_de_anuncios = []
    dados_html = requests.get('http://www.portalmiradouro.com.br/site/category/portal/').content

    barra_lateral_de_anuncios = BeautifulSoup(dados_html, 'html.parser')
    anuncio = barra_lateral_de_anuncios.findAll('img')

    for imagem_de_anuncio in anuncio:
        lista_de_anuncios.append(imagem_de_anuncio['src'])
    return lista_de_anuncios
