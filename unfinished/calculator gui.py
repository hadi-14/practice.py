from tkinter import *

windows = Tk()

windows.config(background="grey")
windows.title("Calculator")
windows.geometry("500x75")

exp1 = ""
expression = ""
exp2 = ""
math = ""


def press(provided):
    global expression

    expression += provided


def ope(operator):
    global expression, exp2, math

    exp2 = expression
    expression = ""
    math = operator


def calculate():
    global expression
    global exp2
    global math

    exp = expression

    if math == "+":
        exp = float(exp) + float(exp2)
    elif math == "-":
        exp = float(exp) - float(exp2)
    elif math == "/":
        exp = float(exp) / float(exp2)
    else:
        exp = float(exp) * float(exp2)

    Textbox1.delete("1.0", END)
    Textbox1.insert(END, exp)


def clear():
    global expression

    expression = ""


Textbox1 = Text(windows)

Textbox1.grid(row=0, column=0)

Button1 = Button(windows, text="9", command=press("9"))
Button2 = Button(windows, text="8", command=press("8"))
Button3 = Button(windows, text="7", command=press("7"))
Button4 = Button(windows, text="6", command=press("6"))
Button5 = Button(windows, text="5", command=press("5"))
Button6 = Button(windows, text="4", command=press("4"))
Button7 = Button(windows, text="3", command=press("3"))
Button8 = Button(windows, text="2", command=press("2"))
Button9 = Button(windows, text="1", command=press("1"))
Button10 = Button(windows, text="0", command=press("0"))
Button11 = Button(windows, text=".", command=press("."))
Button12 = Button(windows, text="+", command=ope("+"))
Button13 = Button(windows, text="-", command=ope("-"))
Button14 = Button(windows, text="x", command=ope("*"))
Button15 = Button(windows, text="÷", command=ope("/"))
Button16 = Button(windows, text="=", command=calculate())
Button17 = Button(windows, text="00", command=press("00"))
Button18 = Button(windows, text="C", command=clear())

Button1.grid(row=1, column=0)
Button2.grid(row=1, column=1)
Button3.grid(row=1, column=2)
Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)
Button7.grid(row=3, column=0)
Button8.grid(row=3, column=1)
Button9.grid(row=3, column=2)
Button10.grid(row=4, column=1)
Button11.grid(row=4, column=0)
Button12.grid(row=1, column=4)
Button13.grid(row=2, column=3)
Button14.grid(row=3, column=3)
Button15.grid(row=3, column=4)
Button16.grid(row=4, column=3)
Button17.grid(row=4, column=2)
Button18.grid(row=1, column=3)

windows.mainloop()
