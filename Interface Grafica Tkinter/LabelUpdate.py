from tkinter import *
from time import strftime
from datetime import datetime, timedelta

class Clock():

    def __init__(self):
        app = Tk()

        clock = Label(app, font="roboto 10 bold", text=strftime('%H:%M:%S'))
        self.x = 1
        clock.place(relx=self.x)

        def get_current_time():
            self.x = self.x-0.02 if self.x > -0.25 else 1

            now = strftime('%H:%M:%S')
            clock.place(relx=self.x)
            if now != clock['text']:
                clock['text'] = now
            clock.after(100,get_current_time)

        get_current_time()
        def btn_press():
            print("time: "+ clock['text'])

        btn = Button(app, text="click", command=btn_press)
        btn.place(relx=0.5, rely=0.9)

        app.mainloop()

class rascunho():
    def __init__(self):

        def calcTime(time1, time2, function):
            time1, time2 = str(time1), str(time2)
            days = 0
            if "," in time1:
                time1= time1.split(",")[1]
                days += self.onlyNum(time1.split(",")[0])
            if "," in time2:
                time2= time2.split(",")[1]
                days += self.onlyNum(time2.split(",")[0])
            time1, time2 = time1.split(":"), time2.split(":")
            time1 = {"hour":int(time1[0]), "minute":int(time1[1])}
            time2 = {"hour":int(time2[0]), "minute":int(time2[1])}

            if function == "current":
                Time = timedelta(hours=time2["hour"], minutes=time2["minute"]) - timedelta(hours=time1["hour"],minutes=time1["minute"])
            elif function == "sum":
                Time = timedelta(hours=time2["hour"], minutes=time2["minute"]) + timedelta(hours=time1["hour"],minutes=time1["minute"])
            return Time
            
        time1 = "00:00"
        time2 = "23:59"
        time3 = "00:00"
        time4 = "23:59"
        total = calcTime(calcTime(time1,time2,"current"),calcTime(time3,time4,"current"),"sum")
        print(total)


    def onlyNum(self, value, diferent=None):
        numbers = "1234567890"
        if diferent != None:
            numbers += diferent
        value = str(value)
        val = ""
        for i in value:
            if i in numbers:
                val += i
        return val
if __name__ == "__main__":
    rascunho()
    #a = timedelta(hours=int("26"), minutes=int("30"))
    #print(a)