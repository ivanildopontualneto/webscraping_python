import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.content

#Extraindo Site
site = BeautifulSoup(content, 'html.parser')

#HTML da Noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    #Titulo
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    #print(titulo.text)
    #print(titulo['href'])

    #Subtitulo
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    if (subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])
news.to_excel('noticias.xlsx', index=False)

# print(news)
