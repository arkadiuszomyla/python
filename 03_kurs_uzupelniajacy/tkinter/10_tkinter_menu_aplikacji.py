import tkinter as tk

window = tk.Tk()

def menuItemSelected():
    print("menu item selected")

def menuItemOpen():
    print("menu item open")

def menuItemSave():
    print("menu item save")

def menuClose():
    quit()

rootMenu = tk.Menu() #główne menu
fileMenu = tk.Menu()
fileMenu.add_command(label="New", command=menuItemSelected)
fileMenu.add_command(label="Open", command=menuItemOpen)
fileMenu.add_command(label="Save", command=menuItemSave)
fileMenu.add_separator()  #dodaje linie rozdzielającą
fileMenu.add_command(label="Close", command=menuClose)

editMenu = tk.Menu()  #dodajemy kolejną zakładke w menu
editMenu.add_command(label="Copy", command=menuItemSelected)
editMenu.add_command(label="Cut", command=menuItemOpen)
editMenu.add_command(label="Paste", command=menuItemSave)

rootMenu.add_cascade(label="File", menu=fileMenu) #dodajemy fileMenu do rootManu
rootMenu.add_cascade(label="Edit", menu=editMenu) #dodajemy fileMenu do rootManu

window.config(menu=rootMenu) #dodaje rootMenu do okna

window.mainloop()