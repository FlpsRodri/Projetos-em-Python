from pytube import YouTube
import requests
from tkinter import *
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
        if resp.lower() == ("s","n"):
            if resp == "n": return True
        else : print("Command Not Found ")
    if quality == 1:
        video.streams.get_highest_resolution().download("Downloads")
        if Continue(): return False
    elif quality == 2:
        video.streams.get_lowest_resolution().download("Downloads")
        if Continue(): return False
    else :
        video.streams.get_audio_only().download("Downloads")
        if Continue(): return False
        
def initt():
    url = input("URL: ")
    if url.lower() in ("exit","sair"): pass # break
    elif verificar_url(url):
        video = YouTube(url)
        title = video.title
        print(f"Video Selecionado: {title} ")
        print("Baixar em: \n1 > Alta Resolução \n2 > Baixa Resolução \n3 > Somente Audio(mp3)")
        tipo = input("num: ")
        try:
            tipo = int(tipo)
        except:
            print("Valor inserido inválido")
            pass #continue
        if tipo not in range(1,4) :
            print("Opção Inválida")
            pass #continue
    if download(video,tipo) == False : pass #break
class app ():

    def __init__(self):
        self.main()
    def main(self):
        self.root = Tk()
        self.root.title("Video Download")
        self.root.geometry("400x500")
        self.root.resizable(False,False)
        self.bg = "white"
        self.root.config(bg=self.bg)
        self.fonte='arial'
        Label(self.root,text="Bem Vindo ao", font=self.fonte+" 12 bold", bg=self.bg).pack(anchor=CENTER)
        Label(self.root,text="YouTube Download", font=self.fonte+" 16 bold", bg=self.bg).pack(anchor=CENTER)

        self.VideoFrame = LabelFrame(self.root, text="VIDEO", bd=2, relief=GROOVE, width=350, height=200, bg=self.bg).pack(anchor=CENTER)
        Label(self.VideoFrame,text="URL do Video", bg=self.bg).place(relx=0.1, rely=0.2)
        URL = Entry(self.VideoFrame, width=35, font=self.fonte, bd=2, bg="#efef88")
        URL.place(relx=0.1, rely=0.25, relheight=0.06)
        self.btnSrch = Button(self.VideoFrame, text="Buscar", font=self.fonte+" 8", command=lambda:self.url_sourche(URL.get())).place(relx=0.79, rely=0.31)
        self.titleVideo = Label(self.VideoFrame, text="https://www.offensive-security.com/pwk-oscp/ ", bg=self.bg, font=self.fonte+" 10 bold")
        self.titleVideo.place(relx=0.13, rely=0.36)

        self.downloadFrame = LabelFrame(self.root, text="Download", bd=2, relief=GROOVE, width=350, height=170, bg=self.bg).pack(anchor=CENTER)
        self.btn_q1 = Button(self.downloadFrame, text="Hight Quality", height=3,command=self.download).place(relx=0.1, rely=0.62)
        self.btn_q2 = Button(self.downloadFrame, text="Low Quality", height=3).place(relx=0.4, rely=0.62)
        self.btn_q3 = Button(self.downloadFrame, text="Only Sound", height=3).place(relx=0.7, rely=0.62)
        self.root.mainloop()

    def url_sourche(self,url):
        try:
            self.video = False
            req = requests.get(url)
            if req.status_code == 200:
                try:
                    self.video = YouTube(url)
                    title = self.video.title
                    if len(title) > 52:
                        Title = ""
                        for i in title:
                            Title += i
                            if len(Title) == 52:
                                Title += "\n"

                        self.titleVideo["text"] = Title
                    else:
                        self.titleVideo["text"] = title
                    return True
                except:
                    return "Endereço URL Invalida"
            else:
                print("Erro na URL")
                return False
        except:
            print("Erro na URL, ou Falha de conexção")
            return False
    def  download(self):
        video.streams.get_highest_resolution().download("Downloads")
if __name__ == '__main__':
    run = initt()
