import tkinter as tk
from tkinter import ttk
#For image handling
from PIL import Image, ImageTk
import PIL
#from gpiozero import LED
from time import sleep

#Root
root = tk.Tk()

#Variiables
window_width = 500
window_height = 300
green_num = 0
blue_num = 0
red_num = 0
#green_label_info = "START"
#led_red = LED(18)
#led_blue = LED()
#led_green = LED()
#led_white = LED()


#Grid parameter confirmation
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

#Functions
def green():
    global green_num
    if (green_num%2) == 0:
        green_num=green_num+1
        tk.Label(root, text='ON').grid(column=1, row=0)
        print('Green LED is on. Clicknumber: '+str(green_num))
    else:
        green_num=green_num+1
        tk.Label(root, text='OFF').grid(column=1, row=0)
        print('Green LED is off. Clicknumber: '+str(green_num))
def blue():
    global blue_num
    if (blue_num%2) == 0:
        blue_num=blue_num+1
        tk.Label(root, text='ON').grid(column=1, row=1)
        print('Blue LED is on. Clicknumber: '+str(blue_num))
    else:
        blue_num=blue_num+1
        tk.Label(root, text='OFF').grid(column=1, row=1)
        print('Blue LED is off. Clicknumber: '+str(blue_num))
def red():
    global red_num
    if (red_num%2) == 0:
        red_num=red_num+1
        tk.Label(root, text='ON').grid(column=1, row=2)
        print('Red LED is on. Clicknumber: '+str(red_num))
    else:
        red_num=red_num+1
        tk.Label(root, text='OFF').grid(column=1, row=2)
        print('Red LED is off. Clicknumber: '+str(red_num))

#Screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)


#Buttons
green_button = ttk.Button(root, text='Green LED', command=lambda: green())
green_button.grid(column=0, row=0, ipadx=50, ipady=30)

blue_button = ttk.Button(root, text='Blue LED', command=lambda: blue())
blue_button.grid(column=0, row=1, ipadx=50, ipady=30)

red_button = ttk.Button(root, text='Red LED', command=lambda: red())
red_button.grid(column=0, row=2, ipadx=50, ipady=30)

#Labels
tk.Label(root, text='OFF').grid(column=1, row=0)
tk.Label(root, text='OFF').grid(column=1, row=1)
tk.Label(root, text='OFF').grid(column=1, row=2)

#Canvas
#canvas = tk.Canvas(root, bg='white', width = 100, height=100)
#canvas.grid(column=2, rowspan=2, sticky=tk.NS)
#Images
green_image = Image.open("Bulb_Images/green100.png")      #importing image from file
green_test = ImageTk.PhotoImage(image1)
green_image_label = tkinter.Label(image=green_test)       #creation of the image label
green_image_label.image = test
green_image_label.grid(column=2, row=0, sticky=tk.N)      #Positioning of the image

root.title('LED Control')
root.resizable(True, True)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.mainloop()
