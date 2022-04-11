from tkinter import *

app = Tk()
app.geometry('350x200')
app.title("Simple Calculator")
resultStr = StringVar()
lbl1 = Label(app, text="First Number: ")
lbl2 = Label(app, text="Second Number: ")
entry1 = Entry(app)
entry2 = Entry(app)
lblResult1 = Label(app, text="Result:  ")
lblResult2 = Label(app, text="", textvariable=resultStr)
lblResult1.grid(row=5, column=0, sticky=W)
lblResult2.grid(row=5, column=1, sticky=W)
entry1.grid(row=0, column=1, sticky=W)
entry2.grid(row=1, column=1, sticky=W)
lbl1.grid(row=0, column=0, sticky=W)
lbl2.grid(row=1, column=0, sticky=W)


def add(a, b):
    print(a + b)
    resultStr.set("")
    resultStr.set(str(a + b))


def sub(a, b):
    resultStr.set("")
    print(a - b)
    resultStr.set(str(a - b))


def mul(a, b):
    resultStr.set("")
    print(a * b)
    resultStr.set(str(a * b))


def div(a, b):
    resultStr.set("")
    print(a / b)
    resultStr.set(str(a / b))


def mod(a, b):
    resultStr.set("")
    print(a % b)
    resultStr.set(str(a % b))


btn1 = Button(app, text="Addition", command=lambda: add(int(entry1.get()), int(entry1.get())))
btn1.grid(row=2, column=0, sticky=W)
btn2 = Button(app, text="Subtraction", command=lambda: sub(int(entry1.get()), int(entry1.get())))
btn2.grid(row=2, column=1, sticky=W)
btn3 = Button(app, text="Multiplication", command=lambda: mul(int(entry1.get()), int(entry1.get())))
btn3.grid(row=3, column=0, sticky=W)
btn4 = Button(app, text="Division", command=lambda: div(int(entry1.get()), int(entry1.get())))
btn4.grid(row=3, column=1, sticky=W)
btn5 = Button(app, text="Reminder", command=lambda: mod(int(entry1.get()), int(entry1.get())))
btn5.grid(row=4, column=0, sticky=W)
btn6 = Button(app, text="Close")
btn6.grid(row=4, column=1, sticky=W)

app.mainloop()
