from tkinter import *
from tkinter import ttk

paint = Tk()
lastx, lasty = 0, 0
color = "Black"
tool = "line"
rec = None
thickness = 5


# functions

def clear(v):
    draw.delete(v)


def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


def line(event):
    global lastx, lasty
    draw.create_line((lastx, lasty, event.x, event.y), fill=color,)
    lastx, lasty = event.x, event.y


def switch_color(p):
    global color
    color = p

def sunken_th(p):
    thick.config(relief = RAISED,bg="#A4CCCB")
    medium.config(relief = RAISED,bg="#A4CCCB")
    thin.config(relief = RAISED,bg="#A4CCCB")
    if p == "thick":
        thick.config(relief=SUNKEN, bg = "gray")
    elif p == "thin":
        thin.config(relief = SUNKEN, bg = "gray")
    elif p == "medium":
        medium.config(relief = SUNKEN, bg = "gray")

def sunken_t(p):
    Pencil.config(relief = RAISED,bg="#A4CCCB")
    Rec.config(relief = RAISED,bg="#A4CCCB")
    brush.config(relief = RAISED,bg="#A4CCCB")
    if p == "rec":
        Rec.config(relief=SUNKEN, bg = "gray")
    elif p == "pencil":
        Pencil.config(relief = SUNKEN, bg = "gray")
    elif p == "brush":
        brush.config(relief = SUNKEN, bg = "gray")

def sunken_c(p):
    red.config(relief=RAISED)
    Black.config(relief=RAISED)
    Blue.config(relief=RAISED)
    Yellow.config(relief=RAISED)
    Green.config(relief=RAISED)
    if p == "red":
        red.config(relief=SUNKEN)
    elif p == "black":
        Black.config(relief=SUNKEN)
    elif p == "blue":
        Blue.config(relief=SUNKEN)
    elif p == "yellow":
        Yellow.config(relief=SUNKEN)
    elif p == "green":
        Green.config(relief=SUNKEN)
    elif p == "orange":
        Orange.config(relief=SUNKEN)


def d_rectangle(event):
    global lastx, lasty, rec
    if rec:
        draw.delete(rec)
    oval = None
    draw.create_rectangle((lastx, lasty, event.x, event.y), fill=color)


def show_rec(event):
    global rec
    if rec:
        draw.delete(rec)
    rec = draw.create_rectangle((lastx, lasty, event.x, event.y), fill=color)

def d_brush(event):
    global lastx, lasty, thickness
    draw.create_line((lastx, lasty, event.x, event.y), fill=color, width = thickness)
    lastx, lasty = event.x, event.y

def c_thick(p):
    global thickness
    thickness = p


def switch_tools(t):
    global tool, draw
    tool = t
    if t == "line":
        draw.bind("<ButtonPress-1>", unbind)
        draw.bind("<ButtonRelease-1>", unbind)
        draw.bind("<Button-1>", xy)
        draw.bind("<B1-Motion>", line)
    if t == "rectangle":
        draw.bind("<Button-1>", unbind)
        draw.bind("<B1-Motion>", show_rec)
        draw.bind("<ButtonPress-1>", xy)
        draw.bind("<ButtonRelease-1>", d_rectangle)
    if t == "brush":
        draw.bind("<ButtonPress-1>", unbind)
        draw.bind("<ButtonRelease-1>", unbind)
        draw.bind("<Button-1>", xy)
        draw.bind("<B1-Motion>", d_brush)


def unbind(event):
    pass


# canvas
draw = Canvas(paint, height=10, width=300)
draw.grid(column=4, row=0, sticky=(N, S), columnspan=4, rowspan=10)

# labels

color_label = Label(paint, bg="#A4CCCB", height=30, width=10)
tool_label = Label(paint, bg="#A4CCCB", height=30, width=10)
c_label = Label(color_label, text="colours", font='Helvetica 14 bold', bg="#A4CCCB", fg="#165A58")
t_label = Label(color_label, text="Tools", font='Helvetica 14 bold', bg="#A4CCCB", fg="#165A58")

# buttons
red = Button(color_label, bg="red", command=lambda: [switch_color("red"), sunken_c("red")], relief=RAISED)
Black = Button(color_label, bg="black", command=lambda: [switch_color("black"), sunken_c("black")], relief=SUNKEN)
Blue = Button(color_label, bg="blue", comman=lambda: [switch_color("blue"), sunken_c("blue")], relief=RAISED)
Yellow = Button(color_label, bg="yellow", command=lambda: [switch_color("yellow"), sunken_c("yellow")], relief=RAISED)
Green = Button(color_label, bg="green", command=lambda: [switch_color("green"), sunken_c("green")], relief=RAISED)
Orange = Button(color_label, bg="orange", command=lambda: [switch_color("orange"), sunken_c("orange")], relief=RAISED)
erase = Button(paint, bg="#A4CCCB", text="Clear all", command=lambda: clear("all"))
Pencil = Button(color_label, bg="gray", text="Line", relief=SUNKEN,command=lambda: [switch_tools("line"),sunken_t("pencil")])
Rec = Button(color_label, bg="#A4CCCB", text="Rectangle", command=lambda: [switch_tools("rectangle"),sunken_t("rec")])
brush = Button(color_label, bg = "#A4CCCB", text = "brush", command = lambda: [switch_tools("brush"),sunken_t("brush")])
thick = Button(color_label,text = "3",bg = "#A4CCCB",command = lambda : [c_thick("15"),sunken_th("thick")])
medium = Button(color_label,text = "2",bg = "#A4CCCB",command = lambda : [c_thick("10"),sunken_th("medium")])
thin = Button(color_label, text = "1",bg = "gray", relief = SUNKEN, command = lambda : [c_thick("5"),sunken_th("thin")])

# placement
color_label.grid(row=0, column=0, rowspan=10, columnspan=3,sticky=(N, E, S, W,))
c_label.grid(row=0, column=0, columnspan=3, sticky=(N, W,))
tool_label.grid(row=0, column=10, rowspan=10, sticky=(N, W,))
t_label.grid(row=3, column=0, columnspan=3, sticky=(N, W, S, E))
Pencil.grid(row=4, column=0, columnspan=3, sticky=(N, W, S, E))
Rec.grid(row=5, column=0, columnspan=3, sticky=(N, W, S, E))
brush.grid(row=6, column=0, columnspan=3, sticky=(N, W, S, E))
erase.grid(row=9, column=0, columnspan=3, sticky=( W, S, E))
thick.grid(row=7, column=2, sticky=(W, E), columnspan=1, rowspan=1)
medium.grid(row=7, column=1, sticky=(W, E), columnspan=1, rowspan=1)
thin.grid(row=7, column=0, sticky=(W, E), columnspan=1, rowspan=1)


red.grid(row=1, column=0, sticky=(W, E), columnspan=1, rowspan=1)
Black.grid(row=1, column=1, sticky=(W, E), columnspan=1, rowspan=1)
Blue.grid(row=1, column=2, sticky=(W, E), columnspan=1, rowspan=1)
Yellow.grid(row=2, column=0, sticky=(W, E), columnspan=2, rowspan=1)
Green.grid(row=2, column=1, sticky=(W, E), columnspan=1, rowspan=1)
Orange.grid(row=2, column=2, sticky=(W, E), columnspan=1, rowspan=1)

draw.bind("<Button-1>", xy)
draw.bind("<B1-Motion>", line)


paint.mainloop()
