from tkinter import *
from tkinter import ttk

root = Tk()


Label(root, text = "Latitude").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text = "Longitude").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)


Button(root, text="Sun").grid(row=3)
Button(root, text="Mercury").grid(row=3, column=1)
Button(root, text="Venus").grid(row=3, column=2)
Button(root, text="Mars").grid(row=3, column=3)
Button(root, text="Jupiter").grid(row=4)
Button(root, text="Saturn").grid(row=4, column=1)
Button(root, text="Uranus").grid(row=4, column=2)
Button(root, text="Neptune").grid(row=4, column=3)



root.mainloop() #keeps window open