from tkinter import *
from tkinter import ttk
from ephem import *
import ephem
import datetime
import os
#calls Planet functions from ephem
usr = Observer()
Sun = Sun(usr)
mercury = Mercury(usr)
Venus = Venus(usr)
Mars = Mars(usr)
Jupiter = Jupiter (usr)
Saturn = Saturn(usr)
Uranus = Uranus(usr)
Neptune = Neptune(usr)


window = Tk()


#---------FUNCTION---------
def marsLocal():
	resultRa = Label(window, text=Mars.ra)
	resultDec = Label(window, text= Mars.dec)
	resultRa.grid(column=10, row=10)
	resultDec.grid(column=10, row=11)
# 
#-------------TITLE--------
Title = Frame(window)
Title.grid(column=0, row=0)
window.title("Plantet Tracker")
wel = "Welcome to Aaron's Planet Tracker\nPlease enter your Latitude and Longitude"
Label1 = Label(Title, text=wel)
Label1.grid( column=0, row=0, sticky="n")



#-----------ENTRIES--------
Label(Title, text="Latitude:").grid(column=0, row=2)
lat=Entry(Title)
lat.grid(column=1, row=2)
Label(Title, text="Longitude:").grid(column=0, row=3)
lon=Entry(Title)
lon.grid(column=1, row=3)

usr.lat = lat.get()
usr.lon = lon.get()

#-----------BUTTONS----------------
Pbuttons = Frame(window)
Pbuttons.grid()
Sun=Button(Pbuttons, height=2, width=6, text="Sun")
Sun.grid(column=0, row=6)
Mer=Button(Pbuttons, height=2, width=6, text="Mercury")
Mer.grid(column=1, row=6)
Ven=Button(Pbuttons, height=2, width=6, text="Venus")
Ven.grid(column=2, row=6)
Mar=Button(Pbuttons, height=2, width=6, text="Mars", command=marsLocal)
Mar.grid(column=3, row=6)
Jup=Button(Pbuttons, height=2, width=6, text="Jupiter")
Jup.grid(column=0, row=7)
Sat=Button(Pbuttons, height=2, width=6, text="Saturn")
Sat.grid(column=1, row=7)
Ura=Button(Pbuttons, height=2, width=6, text="Uranus")
Ura.grid(column=2, row=7)
Nep=Button(Pbuttons, height=2, width=6, text="Neptune")
Nep.grid(column=3, row=7)



window.mainloop() #keeps window open