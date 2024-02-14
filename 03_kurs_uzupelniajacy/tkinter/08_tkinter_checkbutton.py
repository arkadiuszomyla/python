# przycisk wyboru ma dwa stany, włączony lub wyłączony, może posiadać różne wartości - intVar(), StringVar() lub BooleanVar(); onValue - włączone, offValue - wyłączone
import tkinter as tk

window = tk.Tk()


def valueChange():
    if cbValue.get() == 0:
        print("CheckBox is off")
    if cbValue.get() == 1:
        print("CheckBox is on")


cbValue = tk.IntVar(value=0)  # wartość, która będzie przechowywana w buttonie
c1 = tk.Checkbutton(window, text="Accept:", variable=cbValue,
                    onvalue=1, offvalue=0, command=valueChange)

c1.grid(row=0)

window.mainloop()
