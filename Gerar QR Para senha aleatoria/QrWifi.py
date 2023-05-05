import qrcode
import random
from tkinter import *
import os
#import datetime

#base64.guru
class QR():
    def __init__(self):
        self.rede = {"ssid":"ClientesHosted","keyUsage":"persistent","mode":"allow"}
        self.run()

    def onlyNum(self,value, diferent=None):
        numbers = "1234567890"
        if diferent!= None:
            numbers += diferent
        value = str(value)
        val = ""
        for i in value:
            if i in numbers:
                val += i
        return val
    
    def run(self):
        
        #os.system("netsh wlan set hostednetwork mode=allow keyUsage=persistent")
        #command=("netsh wlan set hostednetwork ssid="+self.rede["ssid"])
        #os.system(command)
        #os.system("netsh wlan start hostednetwork")

        self.administer()
        self.gerarQr()
        self.Window()
        

    def administer(self):
        os.system("netsh wlan set hostednetwork mode=allow keyUsage=persistent")
        command=("netsh wlan set hostednetwork ssid="+self.rede["ssid"])
        os.system(command)
        os.system("netsh wlan start hostednetwork")

        def key():
            values = "1234567890abcdefghijklmnopqrstuv"
            value = random.sample(values,k=10)
            self.key=""
            for i in value:self.key+=i
            
            os.system("netsh wlan set hostednetwork key="+self.key)
            with open("temp\config.if","w") as config:
                for i in self.key:
                    config.write(i)
            
            return self.key
        key()
        #print(datetime.datetime.now())

    def gerarQr(self):
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4)
        with open("temp\config.if","r") as config:
            key = config.read()
        key = "WIFI:S:"+self.rede["ssid"]+";T:WPA;P:"+key+";;"
        qr.add_data(key)
        qr.make(fit=True)
        imagem = qr.make_image(fill_color='black',back_color='white')
        imagem.save('temp\qrcodeKey.png')

    def Window(self):
        
        root = Tk()
        root.title("QR Connect-FLPWadminister")
        root.geometry("300x320")

        def qr():
            self.btn.place_forget()
            self.lbl.place(relx=0,rely=0, relheight=0.9, relwidth=1)    
        def logar():
            pass
        def keyFilter(*args):
            self.keyVar.set(self.onlyNum(self.keyVar.get()))
        font="roboto 10 bold"
        self.keyVar = StringVar()
        self.keyVar.trace("w",keyFilter)
        Pass = Entry(root,font=font,width=22,bg="#fff", textvariable=self.keyVar, show="#")
        Pass.place(relx=0.1,rely=0.922)
        btn_log = Button(root,text="Entrar", font="roboto 10 bold",bg = "#ccb", width=10,command=logar).place(relx=0.632, rely=0.922)
        self.btn = Button(root,text="Acessar QR", font="roboto 10 bold",bg = "#ccb", width=30,command=qr)
        self.btn.place(relx=0.1,rely=0.83)
        Pass.focus()
        

        self.image = PhotoImage(file='temp\qrcodeKey.png')
        self.lbl = Label(root,image=self.image, text="")
        
        root.mainloop()

if __name__ == "__main__":
    #try:
    start = QR()
    #os.system("netsh wlan stop hostednetwork")
    #except: quit()
    
