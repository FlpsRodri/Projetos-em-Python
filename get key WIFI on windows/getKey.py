import os
import time
from tkinter import *

class app():
    def __init__(self):
        
        root = Tk()
        root.title("GetKey - version LP1.1")
        root.wm_attributes("-toolwindow",1)
        root.resizable(0,0)
        Label(root, text="""
░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░
░░████████████░░░█████████████████░░░░░░""", fg="red", bg="#000").pack()
        
        os.system("ver > temp.txt")
        with open("temp.txt","r") as version:
            lang = "en" if "version" in (version.read()).lower() else "pt"
        self.get_users()
        try:os.system("del key.txt")
        except Exception as ERROR: print(ERROR)
        for SSID in self.SSID_list:
            self.hacKey(SSID,lang)
        root.mainloop()
        
    def get_users(self):
        def filter_ssid(ssid):
            for i in ssid:
                if i == " ":
                    ssid.replace(i,"")
                else:
                    for i in reversed(ssid):
                        if i == " ": ssid.replace(i,"")
                        else: return ssid[1:]
        os.system('netsh wlan show profile | find ":" > rd.txt')
        time.sleep(1)
        try:
            with open("rd.txt","r") as rd:
                rd = str((rd.read())).split("\n")
        except FileNotFoundError:
            print("File Not Found")
            return
        #os.system('del rd.txt')
        self.SSID_list = []
        for i in rd:
            i = i.split(":")
            if len(i[-1]) > 0:
                i = filter_ssid(i[-1])
                self.SSID_list.append(i)
    def hacKey(self,ssid,lang):
        if lang == "pt":
            command = f'netsh wlan show profile "{ssid}" key=clear | find /i "chave" > temp.txt' 
            os.system(command)
            with open("temp.txt","r") as temp:
                temp = str(temp.read()).replace(" ","")
        else:
            command = f'netsh wlan show profile "{ssid}" key=clear | find /i "key content" > temp.txt' 
            os.system(command)
            with open("temp.txt","r") as temp:
                temp = str(temp.read()).replace(" ","")
        key = temp.split(":")[-1]
        if len(key) < 8: key = "None?\n"
        os.system('del temp.txt | del rd.txt')
        try:
            with open("key.txt","a") as key_file:
                txt  = ssid+" : "+ key
                key_file.write(txt)
        except Exception as ERROR: print(ERROR)
                            
if __name__ == "__main__":
    run = app()
