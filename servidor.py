
from ftplib import FTP

from decouple import config

HOST = config('HOST')
PORTA = config('PORTA', cast=int)
USUARIO = config('USUARIO')
SENHA = config('SENHA')

_conexao_ftp = None


def conectar() -> None:
    """Abre uma conexão com o servidor FTP."""
    global _conexao_ftp
    _conexao_ftp = FTP()
    _conexao_ftp.connect(HOST, PORTA)
    _conexao_ftp.login(user=USUARIO, passwd=SENHA)


def upload(caminho_remoto: str, arquivo_local: str) -> None:
    """
    Envie um arquivo para o servidor

    :param caminho_remoto: Caminho completo do arquivo no servidor
    :param arquivo_local: Caminho completo do arquivo a enviar
    """
    global _conexao_ftp

    with open(arquivo_local, 'rb') as arq:
        _conexao_ftp.storbinary(f'STOR {caminho_remoto}', arq)
