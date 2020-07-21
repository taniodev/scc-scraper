
import os
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup

DIR_BASE = os.path.dirname(os.path.abspath(__file__))
DIR_DE_DOWNLOAD = os.path.join(DIR_BASE, 'download')
CAMINHO_DO_ARQUIVO = os.path.join(DIR_DE_DOWNLOAD, 'scc.zip')


def extrair_zip() -> list:
    """Extraia e retorne uma lista ordenada com o nome dos arquivos extraídos."""
    arquivo_zip = ZipFile(CAMINHO_DO_ARQUIVO, 'r')
    arquivo_zip.extractall(DIR_DE_DOWNLOAD)
    arquivos_extraidos = [x.filename for x in arquivo_zip.infolist()]
    arquivo_zip.close()
    os.remove(CAMINHO_DO_ARQUIVO)

    return sorted(arquivos_extraidos)


def fazer_download(url: str) -> None:
    """Fazer o download do arquivo."""
    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception(f'{resp.status_code} - Falha no download {url}')

    with open(CAMINHO_DO_ARQUIVO, 'wb') as f:
        f.write(resp.content)


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


def renomear_arquivos(nomes_originais: list, novos_nomes: list) -> None:
    """Renomeia os arquivos."""
    for indice, _ in enumerate(nomes_originais):
        arquivo_original = os.path.join(DIR_DE_DOWNLOAD, nomes_originais[indice])
        novo_arquivo = os.path.join(DIR_DE_DOWNLOAD, novos_nomes[indice])
        os.rename(arquivo_original, novo_arquivo)


if __name__ == '__main__':
    url = obter_url()
    fazer_download(url)
    arquivos_extraidos = extrair_zip()

    novos_nomes = [
        '01 - Saude com Ciencia.mp3',
        '02 - Saude com Ciencia.mp3',
        '03 - Saude com Ciencia.mp3',
        '04 - Saude com Ciencia.mp3',
        '05 - Saude com Ciencia.mp3',
    ]

    renomear_arquivos(arquivos_extraidos, novos_nomes)
