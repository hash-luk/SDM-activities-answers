import requests
from pathlib import Path
from bs4 import BeautifulSoup
import re

#1 ) Modifique o seguinte código para retornar a resposta da requisição "GET" em formato XML:
def printInXmlFormat():
    url = "https://viacep.com.br/ws/"
    cep = "30140071"
    formato = "/xml/"
    r = requests.get(url + cep + formato)
    if r.status_code == 200:
        print()
        print("XML : ", r.text)
        print()
    else:
        print("Nao houve sucesso na requisicao.")

#2 ) Modifique o código anterior para que, usando uma estrutura de repetição, consulte 5 CEPs
# sequenciais.
# Suponha que o CEP da sua casa seja 30140-071, o código Python deverá enviar 5 requisições
# com os seguintes CEPs:
# 30140071, 30140072, 30140073, 30140074 e 30140075

def printSusequentCeps():
    url = "https://viacep.com.br/ws/"
    cep = 30140070
    formato = "/json/"

    for c in range(5):
        cep = cep + 1
        r = requests.get(url + str(cep) + formato)
        if r.status_code == 200:
            print()
            print("CEP Buscado:",cep ," ", r.json())
            print()
        else:
            print("Nao houve sucesso na requisicao.")


#3 ) Modifique o código para que a consulta seja feita com um endereço (nome de rua), ao invés
#do CEP.

def searchWithStreetName():
    url = "https://viacep.com.br/ws/MG/Belo Horizonte/"
    street = (input("Digite o endereço: "))
    formato = "/json/"

    r = requests.get(url + street + formato)
    results = r.json()
    print("Endereço Pesquisado: ", street)
    print()
    
    if len(results)> 0:
        for r in results:
            print(r)
    else:
        print(results)

#4) Modifique o primeiro código de tal forma que o endereço " https://viacep.com.br/abc/"
# tente ser acessado. Exiba o código de retorno e o texto.

def printErrorStatus():
    url = "https://viacep.com.br/"
    randomString = "abc"
    formato = "/json/"

    r = requests.get(url + randomString + formato)

    print("Código de retorno: ", r.status_code)
    print("Status: ", r.reason)



#5 ) Modifique-o para que os resultados sejam salvos em arquivo.
def saveResultsInArchive():
    archive = Path('./results.txt')
    archive.touch(exist_ok=True)
    f = open(archive, 'w')

    r = requests.get('http://www.google.com/search', params={'q':'Protocolo HTTP'})

    if (r.status_code == 200):  
        f.write("Conteúdo:" + r.text)
    else:
        f.write("Não foi possível realizar a requisição.")

    f.close()
