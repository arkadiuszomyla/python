import tkinter as tk

window = tk.Tk()

scroollbar = tk.Scrollbar(window)

listBox = tk.Listbox(window, selectmode=tk.MULTIPLE)
# selectmode - MULTIPLE lub SINGLE, opcje zaznaczania

scroollbar.pack(side=tk.RIGHT, fill=tk.Y)
listBox.pack(fill=tk.Y)
scroollbar.config(command=listBox.yview())  #łączymy elementy
listBox.config(yscrollcommand=scroollbar.set)  #łączymy elementy

for i in range(15):
    listBox.insert(tk.END, str(i))   #dodawanie elementów do listy

label = tk.Label(window)
label.pack()

def checkList():
    selection = listBox.curselection()
    label.config(text=str(selection))
    label.after(300, checkList)   #w każdym widżecie można ustawić fukncję after, która po danych milisekundach będzie uruchamia daną funkcje


checkList()
window.mainloop()