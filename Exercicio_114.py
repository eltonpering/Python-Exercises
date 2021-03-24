import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está disponivel no momento.')
else:
    print("Consegui acessar o site com sucesso!")
    print(site.read())