from pytube import YouTube
import requests
# App para download de videos do Youtube atraves do link do video

def verificar_url(url):
    try :
        req = requests.get(url)
        if req.status_code == 200 :
            return True
        else: 
            print("Erro na URL")
            return False
    except :
        print("Erro na URL") 
        return False

def download(video,quality):
    def Continue():
        print("Baixar outro video? (S/N)")
        resp =  input(">> ")
        if resp.lower() in ("s","n"):
            if resp == "n": return False
    if quality == 1:
        video.streams.get_highest_resolution().download("Downloads")
        if Continue() == False : return False
    elif quality == 2:
        video.streams.get_lowest_resolution().download("Downloads")
        if Continue() == False : return False
    else :
        video.streams.get_audio_only().download("Downloads")
        if Continue() == False : return False
        
print("Bem Vindo ao Youtube Download \nPara iniciar insira a URL do video desejado")
while True:
    url = input("URL: ")
    if url.lower() == "exit" or url.lower() == "sair":
        break
    elif verificar_url(url) == False : 
        continue
    
    video = YouTube(url)
    title = video.title
    print(f"Video Selecionado: {title} ")
    print("Baixar em: \n1 > Alta Resolução \n2 > Baixa Resolução \n3 > Somente Audio(mp3)")
    tipo = input("num: ")
    try:
        tipo = int(tipo)
    except:
        print("Valor inserido inválido")
        continue
    if tipo not in (1,2,3) :
        print("Opção Inválida")
        continue
    #video = YouTube(url)
    #title = video.title
    if download(video,tipo) == False : break
    