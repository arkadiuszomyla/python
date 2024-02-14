#winget slider pozwala na wybranie zakresu wartości za pomoca suwaka, argument orent ma wartość tk.VERTICAL lub tk.HORIZONTAL
import tkinter as tk

window = tk.Tk()

value = tk.DoubleVar()  #wartość ustawiana przez suwak
scale = tk.Scale(window, from_=0, to=60,  #wartości od-do
                 orient=tk.VERTICAL, variable=value)
scale.pack(anchor=tk.CENTER)  #centrujemy element

def selected():
    selection = "Value: " + str(value.get())
    label.config(text=selection)
    label.after(200, selected)

label = tk.Label(window)
label.pack()

selected()
window.mainloop()