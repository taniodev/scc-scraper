# scc-scraper
Web scraper para fazer download dos episódios do Saúde com Ciência da Faculdade de Medicina da UFMG

## O que isso faz
1. Baixa o arquivo zip contendo os episódios mais recentes do Saúde com Ciência (última semana);
2. Extrai os arquivos e armazena-os no diretório **download** na raíz do projeto;
3. Faz upload dos arquivos extraídos para um servidor FTP;

Nota: Os arquivos são eliminados do diretório **download** ao fazer upload para o servidor.

## Como usar
Primeiro você precisa instalar as dependências necessárias:
```
pip install -r requirements.txt
```

Certifique-se de que exista um diretório chamado **download** no diretório do projeto,
os arquivos baixados serão salvos neste local.

Crie um arquivo **.env** e edite as informações de acesso ao servidor FTP:
```
cp .env-exemplo .env
```

Execute o módulo **scc.py**:
```
python scc.py
```

Se você não quiser fazer upload dos arquivos para um FTP, basta comentar a linha que chama a função **fazer_upload()** no módulo **scc.py**, os
arquivos permanecerão no diretório **download**.

