import tkinter as tk 

frame = tk.Tk() 
frame.title("TextBox Input") 
frame.geometry('400x200') 
def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp) 
inputtxt = tk.Text(frame, 
                   height = 5, 
                   width = 20) 
  
inputtxt.pack() 
printButton = tk.Button(frame, 
                        text = "Print",  
                        command = printInput) 
printButton.pack() 
lbl = tk.Label(frame, text = "") 
lbl.pack() 
frame.mainloop()