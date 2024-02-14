#pole tekstowe
import tkinter as tk

window = tk.Tk()

tk.Label(window, text="First name").grid(row=0, column=0)

entry = tk.Entry(window)
entry.grid(row=0, column=1)
entry.insert(0, "Hello")   #ustawia wartość początkową


def showData():
    print("Entry data:", entry.get())
    entry.delete(0, "end")  #musimy wskazać ile tekstu chcemy skasować


tk.Button(window, text="show info", command=showData).grid(row=1,column=0)

window.mainloop()