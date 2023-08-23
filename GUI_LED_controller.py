import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gpiozero import LED
from time import sleep

#Root
root = tk.Tk()

#Variiables
window_width = 500
window_height = 300
green_num = 0
blue_num = 0
red_num = 0
led_red = LED(18)
led_blue = LED(23)
led_green = LED(24)
#led_white = LED()

#Images import############################################################################
green_image_on = Image.open("Bulb_Images/green100.png")   #green 
green_test_on = ImageTk.PhotoImage(green_image_on)
blue_image_on = Image.open("Bulb_Images/blue100.png")     #blue
blue_test_on = ImageTk.PhotoImage(blue_image_on)
red_image_on = Image.open("Bulb_Images/red100.png")       #red
red_test_on = ImageTk.PhotoImage(red_image_on)
#white_image_on = Image.open("Bulb_Images/white100.png")  #white
#white_test_on = ImageTk.PhotoImage(white_image_on)
LED_image_off = Image.open("Bulb_Images/off100.png")      #off
LED_test_off = ImageTk.PhotoImage(LED_image_off)

#Default LED images:
LED_off_label1 = tkinter.Label(image=LED_test_off)
LED_off_label2= tkinter.Label(image=LED_test_off)
LED_off_label3= tkinter.Label(image=LED_test_off)
LED_off_label1.grid(column=2, row=0, sticky=tk.N)
LED_off_label2.grid(column=2, row=1, sticky=tk.N)
LED_off_label3.grid(column=2, row=2, sticky=tk.N)
##########################################################################################

#Image localization in Label
#green_image_label = tkinter.Label(image=green_test_on)       
#green_image_label.grid(column=2, row=0, sticky=tk.N)     

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
        green_image_label = tkinter.Label(image=green_test_on)       
        green_image_label.grid(column=2, row=0, sticky=tk.N)
        led_green.on()
        print('Green LED is on. Clicknumber: '+str(green_num))
    else:
        green_num=green_num+1
        tk.Label(root, text='OFF').grid(column=1, row=0)
        LED_off_label = tkinter.Label(image=LED_test_off)      
        LED_off_label.grid(column=2, row=0, sticky=tk.N)
        led_green.off()
        print('Green LED is off. Clicknumber: '+str(green_num))
def blue():
    global blue_num
    if (blue_num%2) == 0:
        blue_num=blue_num+1
        tk.Label(root, text='ON').grid(column=1, row=1)
        blue_image_label = tkinter.Label(image=blue_test_on)
        blue_image_label.grid(column=2, row=1, sticky=tk.N)
        led_blue.on()
        print('Blue LED is on. Clicknumber: '+str(blue_num))
    else:
        blue_num=blue_num+1
        tk.Label(root, text='OFF').grid(column=1, row=1)
        LED_off_label = tkinter.Label(image=LED_test_off)      
        LED_off_label.grid(column=2, row=1, sticky=tk.N)      
        led_blue.off()
        print('Blue LED is off. Clicknumber: '+str(blue_num))
def red():
    global red_num
    if (red_num%2) == 0:
        red_num=red_num+1
        tk.Label(root, text='ON').grid(column=1, row=2)
        red_image_label = tkinter.Label(image=red_test_on)
        red_image_label.grid(column=2, row=2, sticky=tk.N)
        led_red.on()
        print('Red LED is on. Clicknumber: '+str(red_num))
    else:
        red_num=red_num+1
        tk.Label(root, text='OFF').grid(column=1, row=2)
        LED_off_label = tkinter.Label(image=LED_test_off)      
        LED_off_label.grid(column=2, row=2, sticky=tk.N)
        led_red.off()
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

root.title('LED Control')
root.resizable(True, True)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.mainloop()
