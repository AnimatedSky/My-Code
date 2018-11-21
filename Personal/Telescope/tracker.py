import ephem
import datetime
import os
from tkinter import *
from tkinter import ttk

from ephem import *
usr = Observer()
Sun = Sun(usr)
mercury = Mercury(usr)
Venus = Venus(usr)
Mars = Mars(usr)
Jupiter = Jupiter (usr)
Saturn = Saturn(usr)
Uranus = Uranus(usr)
Neptune = Neptune(usr)

 #only works for this time zone
usr.lat = 34.252772#input('enter Latitude: ')
usr.lon = -118.490069#input('enter Longitude: ')


while (usr.date != datetime.datetime.now()):
	os.system('cls')
	usr.date = datetime.datetime.now()
	print('%s \n%s' % (Mars.ra, Mars.dec))
	print('\n %s' % (usr))
	input('press any key to conitnue')