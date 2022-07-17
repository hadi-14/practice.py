from tkinter import *

windows = Tk()

windows.config(background="grey")
windows.title("Weight converter")
windows.geometry("500x75")


def from_kg():
    gram = float(input1_value.get()) * 1000

    pound = float(input1_value.get()) * 2.20462

    ounce = float(input1_value.get()) * 35.274

    textbox1.delete("1.0", END)
    textbox1.insert(END, gram)

    textbox2.delete("1.0", END)
    textbox2.insert(END, pound)

    textbox3.delete("1.0", END)
    textbox3.insert(END, ounce)


label1 = Label(windows, text="Enter value in Kg:")
label2 = Label(windows, text="Grans")
label3 = Label(windows, text="Pounds")
label4 = Label(windows, text="Ounces")

input1_value = StringVar()
input1 = Entry(windows, textvariable=input1_value)

button1 = Button(windows, text="convert", command=from_kg)

textbox1 = Text(windows, height=1, width=20)
textbox2 = Text(windows, height=1, width=20)
textbox3 = Text(windows, height=1, width=20)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=1, column=1)
label4.grid(row=1, column=2)
input1.grid(row=0, column=1)
button1.grid(row=0, column=2)
textbox1.grid(row=2, column=0)
textbox2.grid(row=2, column=1)
textbox3.grid(row=2, column=2)

windows.mainloop()
