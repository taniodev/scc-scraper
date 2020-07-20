
import requests
from bs4 import BeautifulSoup


def obter_url() -> str:
    """Retorne a URL direta para fazer download do arquivo."""
    # Obter a URL que leva para a pagina dos episódios da semana
    html_programas_do_ano = requests.get('https://www.medicina.ufmg.br/radio/programas/')
    soup = BeautifulSoup(html_programas_do_ano.content, 'html.parser')
    div = soup.find_all('div', class_='col-md-2')[3]
    url_programas_da_semana = div.find('a')['href']

    # Obter a URL direta do arquivo zip com os episódios da semana
    html_programas_da_semana = requests.get(url_programas_da_semana)
    soup = BeautifulSoup(html_programas_da_semana.content, 'html.parser')
    url_do_arquivo = soup.find('a', class_='bundle-download')['href']

    return url_do_arquivo
