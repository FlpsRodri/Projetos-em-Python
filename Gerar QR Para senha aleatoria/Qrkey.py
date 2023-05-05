from tkinter import *

class appQr():
    def __init__(self):
        
        app = Tk()
        app.geometry("300x300")
        self.lastTime = ""

        image = PhotoImage(file="temp\qrcodeKey.png")
        self.imagLbl = Label(app,image=image)
        self.imagLbl.pack()
        def img(time):
            with open("temp\configT.if") as CurrentTime:
                Time = CurrentTime.read()
            if time != Time:
                time = Time
                self.image = PhotoImage(file="temp\qrcodeKey.png")
            self.imagLbl["image"]= self.image
            self.imagLbl.after(1000,lambda:img(time))

        time = ""
        img(time)

        app.mainloop()

if __name__ == "__main__":
    start = appQr()
