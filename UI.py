from tkinter import *

window = Tk()


nummer = 0

window.title("Number")

window.geometry('600x400')

label = Label(window, text = nummer)
label.grid(column=0, row=0)
label.config(font=("Arial", 80))
label.place(x=300, y=100, anchor="center")

def pclick():
    global nummer
    nummer +=1
    label.configure(text= nummer)

def mclick():
    global nummer
    nummer -=1
    label.configure(text= nummer)
    
    

pbutton = Button(window, text="+", command=pclick)
 
pbutton.grid(column=1, row=1)
pbutton.config(height = 5, width= 5)
pbutton.place(x=250, y= 250, anchor="center")


mbutton = Button(window, text="-", command=mclick) 
mbutton.grid(column=2, row=1)
mbutton.config(height = 5, width= 5)
mbutton.place(x=350, y= 250, anchor="center")

window.mainloop()
