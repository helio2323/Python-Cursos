import requests
from bs4 import BeautifulSoup
import openpyxl

 #Fazer login no site, se necessário
login_url = 'https://www.eneba.com/login'
payload = {'username': 'seu_nome_de_usuario', 'password': 'sua_senha'}
s = requests.Session()
s.post(login_url, data=payload)

# Acessar a página de jogos da Argentina e da Turquia
argentina_url = 'https://www.eneba.com/br/store/xbox-games?country=Argentina'
turquia_url = 'https://www.eneba.com/br/store/xbox-games?country=Turquia'
argentina_page = s.get(argentina_url)
turquia_page = s.get(turquia_url)

# Analisar o código-fonte da página para identificar os elementos que contêm o nome dos jogos e o link do anúncio
argentina_soup = BeautifulSoup(argentina_page.text, 'html.parser')
turquia_soup = BeautifulSoup(turquia_page.text, 'html.parser')

# Usar o método find_all da biblioteca BeautifulSoup para encontrar todos os elementos que contêm o nome dos jogos e o link do anúncio
argentina_games = argentina_soup.find_all('div', class_='card-item-content')
turquia_games = turquia_soup.find_all('div', class_='card-item-content')

# Criar uma nova planilha do Excel e adicionar as duas colunas ("Nome do Jogo" e "Link do Anúncio") a ela
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'Jogos da Argentina e da Turquia'
worksheet.append(['Nome do Jogo', 'Link do Anúncio'])

# Iterar sobre os elementos encontrados e extrair o nome dos jogos e o link do anúncio
for game in argentina_games + turquia_games:
    name = game.find('span', class_='card-item-title').text
    link = game.find('a')['href']
    worksheet.append([name, link])

# Salvar a planilha do Excel
workbook.save(r'C:\Users\Administrator\Desktop\dados_extraidos.xlsx')