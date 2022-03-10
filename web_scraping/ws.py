from bs4 import BeautifulSoup

import requests

# URL recebe conteúdo da requisição
url = requests.get('https://blog.renkel.com.br').content

# Soup baixa HTML
soup = BeautifulSoup(url, 'html.parser')

# Transforma HTML em String
#print(soup.prettify())

logo = soup.find("span", class_="logo-text")

print(logo.string)

# Mostra tags
print(soup.title)

# Mostra tag em String
print(soup.title.string)

# Mostra tag em String - primeiro a no HTML
print(soup.a)