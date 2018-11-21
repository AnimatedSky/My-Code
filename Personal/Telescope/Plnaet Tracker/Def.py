import tkinter as tk
from tkinter import *
from ephem import *
import ephem


usr = Observer()
Sun = Sun(usr)
Mercury = Mercury(usr)
Venus = Venus(usr)
Mars = Mars(usr)
Jupiter = Jupiter (usr)
Saturn = Saturn(usr)
Uranus = Uranus(usr)
Neptune = Neptune(usr)
LARGE_FONT = ("Verdana", 14)

# class SunP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "The Sun's current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Sun.alt)
# 		resultaz = Label(Result, text= Sun.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Sun.alt,Sun.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()


# class MercP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "Mercury's current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Mercury.alt)
# 		resultaz = Label(Result, text= Mercury.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Mercury.alt,Mercury.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()


# class VenP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "Venus' current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Venus.alt)
# 		resultaz = Label(Result, text= Venus.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Mercury.alt,Mercury.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()


# class MarsP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "Mars' current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Mars.alt)
# 		resultaz = Label(Result, text= Mars.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Venus.alt,Venus.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()


# class JupP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "Jupiter's current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Jupiter.alt)
# 		resultaz = Label(Result, text= Jupiter.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Jupiter.alt, Jupiter.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()

# class SatP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "Saturn's current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Saturn.alt)
# 		resultaz = Label(Result, text= Saturn.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Saturn.alt,Saturn.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()

# class UraP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "Uranus' current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Uranus.alt)
# 		resultaz = Label(Result, text= Uranus.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Uranus.alt,Uranus.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()


# class NepP(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self,parent)
# 		wel = "Neptune's current location is"
# 		label = tk.Label(self, text=wel, font=LARGE_FONT)
# 		Result = Frame(self)
# 		Result.grid()
# 		resultalt = Label(Result, text=Neptune.alt)
# 		resultaz = Label(Result, text= Neptune.az)
# 		resultalt.grid()
# 		resultaz.grid()
# 		button1 = tk.Button(Result, height=1, text="Return to Menu",
# 			command=lambda: controller.show_frame(PageTwo))
# 		button1.grid()

# 		f = Figure(figsize=(10,5), dpi=100)
# 		a = f.add_subplot(111)
# 		a.plot(Neptune.alt,Neptune.az, 'ro')

# 		canvas = FigureCanvasTkAgg(f, self)
# 		canvas.show()
# 		canvas.get_tk_widget().grid()

