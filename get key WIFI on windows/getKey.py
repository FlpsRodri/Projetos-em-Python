import os
import time
class app():
    def __init__(self):
        
        #root = Tk()
        #root.title("GetKey - version LP1.0")
        #root.wm_attributes("-toolwindow",1)
        #root.geometry("400
        #root.mainloop()
        os.system('netsh wlan show profile | find ":" > rd.txt')
        time.sleep(1)
        try:
            with open("rd.txt","r") as rd:
                rd = str((rd.read())).split("\n")
        except FileNotFoundError:
            print("File Not Found")
            return
        os.system('del rd.txt')
        SSID_list = []
        Redes = {}
        for i in rd:
            i = i.split(":")
            if len(i[-1]) > 0:
                SSID_list.append(i[-1])
        for SSID in SSID_list:
            SSID = SSID.replace(" ","")
            command = f'netsh wlan show profile "{SSID}" key=clear | find /i "chave" > temp.txt' 
            os.system(command)
            with open("temp.txt","r") as temp:
                temp = str(temp.read()).replace(" ","")
            Redes[SSID] = temp
            os.system('del temp.txt')
        #for i in Redes: print(i, Redes[i])

        try:
            with open("key.txt","r"):
                k = True
            os.system("del key.txt")
            with open("key.txt","a") as key:
                for i in Redes:
                    txt  = i+" : "+ Redes[i]
                    key.write(txt+"\n")
                    print(i,Redes[i])
        except:
            
            with open("key.txt","a") as key:
                txt  = i+Redes[i]
                key.write(txt)
                
            
if __name__ == "__main__":
    run = app()
