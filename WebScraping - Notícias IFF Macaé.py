# APLICANDO NO SITE DO IFF

# RECOMENDO ABRIR COM A IDLE DO PYTHON, POIS SÃO MUITAS NOTÍCIAS,
# E PELO CMD ACABA APAGANDO AS PRIMEIRAS

# 1º PRECSAMOS OBTER O HTML COM O MODULO REQUESTS

import requests

from bs4 import BeautifulSoup

r = requests.get('http://portal1.iff.edu.br/nossos-campi/macae/noticias')

s = BeautifulSoup(r.content, "html.parser")

"""
 Vamos obter cada elemento a que possua
 o atributo class com valor igual a "title ".
 Podemos fazer isso usando o método findAll(),
 percorrendo o resultado e extraindo os atributos
 que nos interessam (href e text):
"""

print("\n############################ NOTÍCIAS IFF MACAÉ #############################")

n = 1 # CONTADOR DE NOTICIAS

for a in s.findAll('a', attrs={'class': 'summary url'}):

    print()

    print("."*77)

    print("\nNotícia", n,  ":\n\n")
    
    print(a.text)

    print("\n\n")

    print('link: ', a.get('href'))

    print("\n")

    n += 1
    print("."*77)

    print()

import os

os.system('pause')
