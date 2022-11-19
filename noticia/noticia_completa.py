from noticia.titulos import titulos
from noticia.datas import datas
from noticia.links import links
from noticia.imagens import imagens


def noticia_completa():
    lista_de_noticias = []
    for x in range(10):
        lista_de_noticias.append({'titulo': titulos()[x]})
        lista_de_noticias[x].update({'link': links()[x]})
        lista_de_noticias[x].update({'data': datas()[x]})
        lista_de_noticias[x].update({'imagens': imagens()[x]})

    return lista_de_noticias

