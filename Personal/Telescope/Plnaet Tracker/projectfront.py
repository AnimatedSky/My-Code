import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg") #matplotlib backend
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import ttk
from ephem import *
from Def import *
import time

import ephem




class PlanetTrakerApp (tk.Tk):
	def __init__(self, *args, **kwargs): #initallizes everytime you run
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self,"Planet Tracker")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, SunP, MercP, VenP, MarsP, JupP, SatP, UraP, NepP): #add pages in for loop
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


#------------FRONT PAGE-----------
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		wel = "Welcome to Aaron's Planet Tracker\nPlease enter your Latitude and Longitude"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		label.grid(column=0, row=0)

		
		Lat_Long = Frame(self)
		Lat_Long.grid()

		Label(Lat_Long, text="Latitude:").grid(column=0, row=2)
		lat=Entry(Lat_Long)
		lat.grid(column=1, row=2)
		Label(Lat_Long, text="Longitude:").grid(column=0, row=3)
		lon=Entry(Lat_Long)
		lon.grid(column=1, row=3)
		Label(Lat_Long, text="Elevation:").grid(column=0, row=4)
		elev=Entry(Lat_Long)
		elev.grid(column=1, row=4)

		usr.lat = lat.get()
		usr.lon = lon.get()
		int_ans = elev.get()
		int_ans = usr.elevation


		button1 = ttk.Button(self, text="Continue", 
			command=lambda: controller.show_frame(PageOne))
		button1.grid()
	

#-------PAGE 1----------
class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		ttk.Frame.__init__(self,parent)
		wel = "Is the Telescope Allign to Polaris?"
		label = ttk.Label(self, text=wel, font=LARGE_FONT)
		label.grid()

		Pbuttons = Frame(self)

		Pbuttons.grid()
		button1 = ttk.Button(Pbuttons, text="no", 
			command=lambda: controller.show_frame(StartPage))
		button1.grid(column=0, row=1)

		button2 = ttk.Button(Pbuttons, text="yes", 
			command=lambda: controller.show_frame(PageTwo))
		button2.grid(column=1, row=1)


#-------PAGE 2----------
class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		Title = Frame(self) 
		label = ttk.Label(self, text="Select a planet", font=LARGE_FONT)
		label.grid(column=0, row=0)

		
		Pbuttons = Frame(self)
		Pbuttons.grid()

		button1 = tk.Button(Pbuttons, height=1, width=6, text="Sun",
			command=lambda: controller.show_frame(SunP))
		button1.grid(column=0, row=6)
		
		button2 = tk.Button(Pbuttons, height=1, width=6, text="Mercury",
			command=lambda: controller.show_frame(MercP))
		button2.grid(column=1, row=6)

		button3 = tk.Button(Pbuttons, height=1, width=6, text="Venus",
			command=lambda: controller.show_frame(VenP))
		button3.grid(column=2, row=6)

		button4 = tk.Button(Pbuttons, height=1, width=6, text="Mars",
			command=lambda: controller.show_frame(MarsP))
		button4.grid(column=3, row=6)

		button5 = tk.Button(Pbuttons, height=1, width=6, text="Jupiter",
			command=lambda: controller.show_frame(JupP))
		button5.grid(column=4, row=6)

		button6 = tk.Button(Pbuttons, height=1, width=6, text="Saturn",
			command=lambda: controller.show_frame(SatP))
		button6.grid(column=5, row=6)

		button7 = tk.Button(Pbuttons, height=1, width=6, text="Uranus",
			command=lambda: controller.show_frame(UraP))
		button7.grid(column=6, row=6)

		button8 = tk.Button(Pbuttons, height=1, width=6, text="Neptune",
			command=lambda: controller.show_frame(NepP))
		button8.grid(column=7, row=6)



#----------------Planet PAGEs--------------------
class SunP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Sun's current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Sun.ra)
		resultaz = Label(Result, text= Sun.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()



class MercP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Mercury's current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Mercury.ra)
		resultaz = Label(Result, text= Mercury.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()



class VenP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Venus' current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Venus.ra)
		resultaz = Label(Result, text= Venus.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()



class MarsP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Mars' current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Mars.ra)
		resultaz = Label(Result, text= Mars.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()




class JupP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Jupiter's current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Jupiter.ra)
		resultaz = Label(Result, text= Jupiter.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()



class SatP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Saturn's current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Saturn.ra)
		resultaz = Label(Result, text= Saturn.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()



class UraP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Uranus' current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Uranus.ra)
		resultaz = Label(Result, text= Uranus.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()



class NepP(tk.Frame):
	def __init__(self, parent, controller):
		time.time = usr.date
		Mars.compute(usr)

		tk.Frame.__init__(self,parent)
		wel = "Neptune's current location is"
		label = tk.Label(self, text=wel, font=LARGE_FONT)
		Result = Frame(self)
		Result.grid()
		resultalt = Label(Result, text=Neptune.ra)
		resultaz = Label(Result, text= Neptune.dec)
		resultalt.grid()
		resultaz.grid()


		button1 = tk.Button(Result, height=1, text="Return to Menu",
			command=lambda: controller.show_frame(PageTwo))
		button1.grid()








app = PlanetTrakerApp()
app.mainloop()




