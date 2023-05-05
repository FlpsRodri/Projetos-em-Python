import requests

def download(url,endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereço, "wb") as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


if __name__ == "__main__":
    download("url do arquivo", "c:\users\public\downloads\{nome_arquivo.*}")
