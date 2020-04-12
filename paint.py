from tkinter import *
from tkinter import ttk

paint = Tk()
lastx , lasty = 0,0
color = "Black"


# functions

def xy(event):
    global lastx , lasty
    lastx , lasty = event.x, event.y

def line(event):
    global lastx , lasty
    draw.create_line((lastx,lasty,event.x,event.y), fill = color)
    lastx , lasty = event.x,event.y

def switch_color(p):
    global color
    color = p

def sunken(p):
    red.config(relief=RAISED)
    Black.config(relief=RAISED)
    Blue.config(relief=RAISED)
    Yellow.config(relief=RAISED)
    Green.config(relief=RAISED)
    if p == "red":
        red.config(relief = SUNKEN )
    elif p == "black":
        Black.config(relief = SUNKEN)
    elif p == "blue":
        Blue.config(relief = SUNKEN)
    elif p == "yellow":
        Yellow.config(relief = SUNKEN)
    elif p == "green":
        Green.config(relief = SUNKEN)


# labels

color_label = Label(paint, bg = "#A4CCCB", height = 30 , width = 10)
draw = Canvas(paint, height = 10 , width = 300)
tool_label = Label(paint, bg = "#A4CCCB", height = 30 , width = 10)
c_label = Label(color_label,text = "colours",font='Helvetica 14 bold', bg = "#A4CCCB",fg="#165A58")

# buttons
red = Button(color_label , bg = "red",command = lambda: [switch_color("red"), sunken("red")],relief=RAISED)
Black = Button(color_label,  bg = "black",command = lambda: [switch_color("black"), sunken("black")],relief=SUNKEN )
Blue = Button(color_label,  bg = "blue", comman = lambda: [switch_color("blue"), sunken("blue")],relief=RAISED)
Yellow = Button(color_label, bg = "yellow", command = lambda: [switch_color("yellow"), sunken("yellow")],relief=RAISED)
Green = Button(color_label, bg = "green", command = lambda: [switch_color("green"), sunken("green")],relief=RAISED)

# placement
color_label.grid(row = 0, column = 0, rowspan = 10,sticky=(N, E, S, W,))
draw.grid(column=4, row=0, sticky=(N, S) ,columnspan = 4, rowspan = 10)
tool_label.grid(row = 0, column = 10, rowspan = 10,sticky=(N, W,))
c_label.grid(row = 0 , column = 0, columnspan = 5)


red.grid(row = 1 , column = 0,sticky=(W,E), columnspan = 1, rowspan = 1)
Black.grid(row = 1 , column = 1,sticky=(W,E),columnspan = 1, rowspan = 1)
Blue.grid(row = 1 , column = 2,sticky=(W,E),columnspan = 1, rowspan = 1)
Yellow.grid(row = 2 , column = 0,sticky=(W,E),columnspan = 2, rowspan = 1)
Green.grid(row = 2 , column = 1,sticky=(W,E),columnspan = 1, rowspan = 1)

draw.bind("<Button-1>", xy)
draw.bind("<B1-Motion>", line)


paint.mainloop()
