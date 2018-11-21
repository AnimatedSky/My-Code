#!/usr/bin/env python3

from tkinter import *
import RPi.GPIO as GPIO
import time
import datetime
import threading
import ephem
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

step_pin_az = 27
dir_pin_az = 23
enable_pin_az = 17
step_pin_alt = 15
dir_pin_alt = 14
enable_pin_alt = 18

GPIO.setup(step_pin_az, GPIO.OUT)
GPIO.setup(dir_pin_az, GPIO.OUT)
GPIO.setup(enable_pin_az, GPIO.OUT)
GPIO.setup(step_pin_alt, GPIO.OUT)
GPIO.setup(dir_pin_alt, GPIO.OUT)
GPIO.setup(enable_pin_alt, GPIO.OUT)

GPIO.output(enable_pin_az, GPIO.LOW)
GPIO.output(enable_pin_alt, GPIO.LOW)

root = Tk()
root.title("Celestial Target Tracker")

global az_tel_steps, alt_tel_steps
alt_tel_degrees = DoubleVar()
az_tel_degrees = DoubleVar()
az_tel_steps = IntVar()
alt_tel_steps = IntVar()
global goto_steps
goto_steps = IntVar()
global target_right_accension, target_declination
global observer_long, observer_lat, observer_elev
global motor_lock_check
global cur_index, target_name
target_name = StringVar()


##Load targets from file for target list
##and generate sorted list for listbox
with open('celestial_object_list.json') as f_obj:
    target_dict = json.load(f_obj)
    
target_name_list = []

for key in target_dict.keys():
	target_name_list.append(key)

target_name_list.sort()
##

def move_left(event):
        az_tel_steps.set(az_tel_steps.get() - 1)
        GPIO.output(dir_pin_az, GPIO.LOW)
        GPIO.output(step_pin_az, GPIO.HIGH)
        GPIO.output(step_pin_az, GPIO.LOW)

def move_right(event):
        az_tel_steps.set(az_tel_steps.get() + 1)
        GPIO.output(dir_pin_az, GPIO.HIGH)
        GPIO.output(step_pin_az, GPIO.HIGH)
        GPIO.output(step_pin_az, GPIO.LOW)

def move_up(event):
        alt_tel_steps.set(alt_tel_steps.get() + 1)
        GPIO.output(dir_pin_alt, GPIO.HIGH)
        GPIO.output(step_pin_alt, GPIO.HIGH)
        GPIO.output(step_pin_alt, GPIO.LOW)

def move_down(event):
        alt_tel_steps.set(alt_tel_steps.get() - 1)
        GPIO.output(dir_pin_alt, GPIO.LOW)
        GPIO.output(step_pin_alt, GPIO.HIGH)
        GPIO.output(step_pin_alt, GPIO.LOW)

## set target RA and DEC to current listbox selection
def set_target():
    cur_index = target_list_listbox.curselection()
    target_coord = target_dict[target_name_list[cur_index[0]]]
    target_name.set(target_name_list[cur_index[0]])
    target_right_accension.set(target_coord[0])
    target_declination.set(target_coord[1])
##

## set telescope position to RA and DEC in target entry boxes    
def align_telescope():
        if messagebox.askyesno(message="Are you sure you want to reset telescope alignment?"):
                telescope = ephem.Observer()
                telescope.long = ephem.degrees(observer_long.get())
                telescope.lat = ephem.degrees(observer_lat.get())
                telescope.elevation = observer_elev.get()

                target = ephem.FixedBody()
                target._ra = target_right_accension.get()
                target._dec = target_declination.get()

                telescope.date = datetime.datetime.utcnow()
                target.compute(telescope)
                az_tel_steps.set(int(target.az * (180 / 3.14159) * 80))
                alt_tel_steps.set(int(target.alt * (180 / 3.14159) * 80))

                messagebox.showinfo(message="Telescope aligned to current target")
##

## disable stepper motors for manual slew    
def motor_unlock():
    
    if motor_lock.get() == True:
        GPIO.output(enable_pin_az, GPIO.HIGH)
        GPIO.output(enable_pin_alt, GPIO.HIGH)
    else:
        GPIO.output(enable_pin_az, GPIO.LOW)
        GPIO.output(enable_pin_alt, GPIO.LOW)
##

## Start stepper drivers in separate threads to allow GUI to continue looping        
def step_driver_thread():
    
    step_thread_az = threading.Thread(target=az_step_driver)
    step_thread_az.start()
    step_thread_alt = threading.Thread(target=alt_step_driver)
    step_thread_alt.start()
##

## azimuth stepper motor driver. further commenting on operation of driver can
## be found in 102516 linear accel stepp driver.py
def az_step_driver():

    motor_lock_check.config(state=DISABLED)
    set_target_button.config(state=DISABLED)
    align_button.config(state=DISABLED)
    motor_lock.set(0)
    
    dir_az = 0
    time_1_az = 0
    time_2_az = 0
    acc_az = 500 
    vel_max_az = 1000
    error_az = 0
    step_time_az = []
    
    telescope = ephem.Observer()
    telescope.long = ephem.degrees(observer_long.get())
    telescope.lat = ephem.degrees(observer_lat.get())
    telescope.elevation = observer_elev.get()

    if target_name.get() == 'Moon':
        target = ephem.Moon()
    elif target_name.get() == 'Mercury':
        target = ephem.Mercury()
    elif target_name.get() == 'Venus':
        target = ephem.Venus()
    elif target_name.get() == 'Mars':
        target = ephem.Mars()
    elif target_name.get() == 'Jupiter':
        target = ephem.Jupiter()
    elif target_name.get() == 'Saturn':
        target = ephem.Saturn()
    elif target_name.get() == 'Uranus':
        target = ephem.Uranus()
    elif target_name.get() == 'Neptune':
        target = ephem.Neptune()
    elif target_name.get() == 'Pluto':
        target = ephem.Pluto()
    else:
        target = ephem.FixedBody()
        target._ra = target_right_accension.get()
        target._dec = target_declination.get()

    GPIO.output(enable_pin_az, GPIO.LOW)

    while track_target.get():
        telescope.date = datetime.datetime.utcnow()
        target.compute(telescope)
        target_steps_az = int(target.az * (180 / 3.14159) * 80)
        az_tel_degrees.set(round(target.az *(180 / 3.14159), 8))

        if target.alt < 0:
                messagebox.showinfo(message="Target is below horizon")
                break
        
        error_az = target_steps_az - az_tel_steps.get()

        if error_az > 0:
            dir_az = 1 
            GPIO.output(dir_pin_az, GPIO.HIGH)
            
        else:
            dir_az = -1 
            error_az = -error_az 
            GPIO.output(dir_pin_az, GPIO.LOW)

        if error_az <= 10:  
            while az_tel_steps.get() != target_steps_az:
                GPIO.output(step_pin_az, GPIO.HIGH)
                GPIO.output(step_pin_az, GPIO.LOW)
                time.sleep(0.1)
                az_tel_steps.set(az_tel_steps.get() + dir_az)

        elif error_az <= 2 * vel_max_az:
            dis_az = 0
            step_time_az = []
            time_1_az = 0
            time_2_az = 0

            while dis_az < int(error_az / 2):
                dis_az += 1
                time_1_az = ((2 * dis_az) / acc_az) ** 0.5
                step_time_az.append(time_1_az-time_2_az)
                time_2_az = time_1_az

            for delta_t_az in step_time_az:
                GPIO.output(step_pin_az, GPIO.HIGH)
                GPIO.output(step_pin_az, GPIO.LOW)
                time.sleep(delta_t_az)
                az_tel_steps.set(az_tel_steps.get() + dir_az)

            step_time_az.reverse() 

            for delta_t_az in step_time_az:
                GPIO.output(step_pin_az, GPIO.HIGH)
                GPIO.output(step_pin_az, GPIO.LOW)
                time.sleep(delta_t_az)
                az_tel_steps.set(az_tel_steps.get() + dir_az)

        elif error_az > 2 * vel_max_az:
            dis_az = 0
            step_time_az = []
            time_1_az = 0
            time_2_az = 0

            while time_1_az < vel_max_az / acc_az:
                dis_az += 1
                time_1_az = ((2 * dis_az) / acc_az) ** 0.5
                step_time_az.append(time_1_az-time_2_az)
                time_2_az = time_1_az

            for delta_t_az in step_time_az:
                GPIO.output(step_pin_az, GPIO.HIGH)
                GPIO.output(step_pin_az, GPIO.LOW)
                time.sleep(delta_t_az)
                az_tel_steps.set(az_tel_steps.get() + dir_az)

            for _az in range(error_az - (2 * vel_max_az)): 
                GPIO.output(step_pin_az, GPIO.HIGH)
                GPIO.output(step_pin_az, GPIO.LOW)
                time.sleep(1 / vel_max_az)
                az_tel_steps.set(az_tel_steps.get() + dir_az)

            step_time_az.reverse()

            for delta_t_az in step_time_az:  
                GPIO.output(step_pin_az, GPIO.HIGH)
                GPIO.output(step_pin_az, GPIO.LOW)
                time.sleep(delta_t_az)
                az_tel_steps.set(az_tel_steps.get() + dir_az)
                
    motor_lock_check.config(state=NORMAL)
    set_target_button.config(state=NORMAL)
    align_button.config(state=NORMAL)
##

## altitude stepper motor driver    
def alt_step_driver():
    
    dir_alt = 0
    time_1_alt = 0
    time_2_alt = 0
    acc_alt = 500 
    vel_max_alt = 1000
    error_alt = 0
    step_time_alt = []
    
    telescope = ephem.Observer()
    telescope.long = ephem.degrees(observer_long.get())
    telescope.lat = ephem.degrees(observer_lat.get())
    telescope.elevation = observer_elev.get()

    if target_name.get() == 'Moon':
        target = ephem.Moon()
    elif target_name.get() == 'Mercury':
        target = ephem.Mercury()
    elif target_name.get() == 'Venus':
        target = ephem.Venus()
    elif target_name.get() == 'Mars':
        target = ephem.Mars()
    elif target_name.get() == 'Jupiter':
        target = ephem.Jupiter()
    elif target_name.get() == 'Saturn':
        target = ephem.Saturn()
    elif target_name.get() == 'Uranus':
        target = ephem.Uranus()
    elif target_name.get() == 'Neptune':
        target = ephem.Neptune()
    elif target_name.get() == 'Pluto':
        target = ephem.Pluto()
    else:
        target = ephem.FixedBody()
        target._ra = target_right_accension.get()
        target._dec = target_declination.get()

    GPIO.output(enable_pin_alt, GPIO.LOW)

    while track_target.get():
        telescope.date = datetime.datetime.utcnow()
        target.compute(telescope)
        target_steps_alt = int(target.alt * (180 / 3.14159) * 80)

        if target.alt < 0:
                break
        
        error_alt = target_steps_alt - alt_tel_steps.get()
        alt_tel_degrees.set(round(target.alt * (180 / 3.14159), 8))
        
        if error_alt > 0:
            dir_alt = 1 
            GPIO.output(dir_pin_alt, GPIO.HIGH)
            
        else:
            dir_alt = -1 
            error_alt = -error_alt 
            GPIO.output(dir_pin_alt, GPIO.LOW)

        if error_alt <= 10:  
            while alt_tel_steps.get() != target_steps_alt:
                GPIO.output(step_pin_alt, GPIO.HIGH)
                GPIO.output(step_pin_alt, GPIO.LOW)
                time.sleep(0.1)
                alt_tel_steps.set(alt_tel_steps.get() + dir_alt)

        elif error_alt <= 2 * vel_max_alt:
            dis_alt = 0
            step_time_alt = []
            time_1_alt = 0
            time_2_alt = 0

            while dis_alt < int(error_alt / 2):
                dis_alt += 1
                time_1_alt = ((2 * dis_alt) / acc_alt) ** 0.5
                step_time_alt.append(time_1_alt-time_2_alt)
                time_2_alt = time_1_alt

            for delta_t_alt in step_time_alt:
                GPIO.output(step_pin_alt, GPIO.HIGH)
                GPIO.output(step_pin_alt, GPIO.LOW)
                time.sleep(delta_t_alt)
                alt_tel_steps.set(alt_tel_steps.get() + dir_alt)

            step_time_alt.reverse() 

            for delta_t_alt in step_time_alt:
                GPIO.output(step_pin_alt, GPIO.HIGH)
                GPIO.output(step_pin_alt, GPIO.LOW)
                time.sleep(delta_t_alt)
                alt_tel_steps.set(alt_tel_steps.get() + dir_alt)

        elif error_alt > 2 * vel_max_alt:
            dis_alt = 0
            step_time_alt = []
            time_1_alt = 0
            time_2_alt = 0

            while time_1_alt < vel_max_alt / acc_alt:
                dis_alt += 1
                time_1_alt = ((2 * dis_alt) / acc_alt) ** 0.5
                step_time_alt.append(time_1_alt-time_2_alt)
                time_2_alt = time_1_alt

            for delta_t_alt in step_time_alt:
                GPIO.output(step_pin_alt, GPIO.HIGH)
                GPIO.output(step_pin_alt, GPIO.LOW)
                time.sleep(delta_t_alt)
                alt_tel_steps.set(alt_tel_steps.get() + dir_alt)

            for _alt in range(error_alt - (2 * vel_max_alt)): 
                GPIO.output(step_pin_alt, GPIO.HIGH)
                GPIO.output(step_pin_alt, GPIO.LOW)
                time.sleep(1 / vel_max_alt)
                alt_tel_steps.set(alt_tel_steps.get() + dir_alt)

            step_time_alt.reverse()

            for delta_t_alt in step_time_alt:  
                GPIO.output(step_pin_alt, GPIO.HIGH)
                GPIO.output(step_pin_alt, GPIO.LOW)
                time.sleep(delta_t_alt)
                alt_tel_steps.set(alt_tel_steps.get() + dir_alt)

root.geometry("480x320")

mainframe = Frame(root)
mainframe.grid(sticky=(N, W, E, S))

Label(mainframe, text="Target:").grid(column=1, row=0, sticky=(W, E))

target_right_accension = StringVar()
right_accension_entry = Entry(mainframe, width=11,
                              textvariable = target_right_accension)
right_accension_entry.grid(column=1, row=1, sticky=(W, E))
Label(mainframe, text="RA:").grid(column=0, row=1, sticky=(E))

target_declination = StringVar()
declination_entry = Entry(mainframe, width=11,
                          textvariable = target_declination)
declination_entry.grid(column=1, row=2, sticky=(W, E))
Label(mainframe, text="Dec:").grid(column=0, row=2, sticky=(E))

track_target = BooleanVar()
track_target_check = Checkbutton(mainframe, variable=track_target,
                                 text="Track Target", pady=15, bg="grey",
                                 command=step_driver_thread)
track_target_check.grid(column=0, row=3, sticky=(W, E), columnspan=2)

Label(mainframe, text="Observer:").grid(column=1, row=4, sticky=(W, E))

Label(mainframe, text="Long:").grid(column=0, row=5, sticky=(E))
observer_long = StringVar(value='-87.852444')
observer_long_entry = Entry(mainframe, width=11,textvariable=observer_long)
observer_long_entry.grid(column=1, row=5, sticky=(W, E))

Label(mainframe, text="Lat:").grid(column=0, row=6, sticky=(E))
observer_lat = StringVar(value='41.256066')
observer_lat_entry = Entry(mainframe, width=11, textvariable=observer_lat)
observer_lat_entry.grid(column=1, row=6, sticky=(W, E))

Label(mainframe, text="Elev(m):").grid(column=0, row=7, sticky=(E))
observer_elev = IntVar(value=205)
observer_elev_entry = Entry(mainframe, width=11, textvariable=observer_elev)
observer_elev_entry.grid(column=1, row=7, sticky=(W, E))

align_button = Button(mainframe, text="Align", command=align_telescope,
                      height=2)
align_button.grid(column=0, row=8, columnspan=2, sticky=(W, E))

motor_lock = BooleanVar()
motor_lock_check = Checkbutton(mainframe, variable=motor_lock,
                               text="Motor Unlock", pady=15, bg="grey",
                               command=motor_unlock)
motor_lock_check.grid(column=0, row=9, sticky=(W, E), columnspan=2)


target_list_listbox = Listbox(mainframe, height=8)
target_list_listbox.grid(column=2, row=1, rowspan=8
                         , sticky=(W, N, E, S))
Label(mainframe, text="Target List:").grid(column=2, row=0, sticky=(W, E))

##Fill listbox with list of targets generated from loaded file
for name in target_name_list:
    target_list_listbox.insert(END, name)
##


set_target_button = Button(mainframe, text="Set Target", command=set_target,
                           height=2)
set_target_button.grid(column=2, row=9, sticky=(W, E), columnspan=2)

set_target_scroll = Scrollbar(mainframe, orient=VERTICAL,
                              command = target_list_listbox.yview,
                              width=25)
set_target_scroll.grid(column=3, row=1, sticky=(N, S), rowspan=8)
target_list_listbox.configure(yscrollcommand=set_target_scroll.set)


Label(mainframe, text="Telescope:").grid(column=5, row=0, sticky=(W, E))
Label(mainframe, text="ALT:").grid(column=4, row=1)
Entry(mainframe, textvariable=alt_tel_degrees, width=10).grid(column=5, row=1,
                                                              sticky=(W, E))

Label(mainframe, text="AZ:").grid(column=4, row=2, sticky=(W, E))
Entry(mainframe, textvariable=az_tel_degrees, width=10).grid(column=5, row=2,
                                                              sticky=(W, E, N))

root.bind("<Shift-Left>", move_left)
root.bind("<Shift-Right>", move_right)
root.bind("<Shift-Up>", move_up)
root.bind("<Shift-Down>", move_down)

root.mainloop()
