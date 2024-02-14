# umożliwia rozmieszczanie elementów w blokach wewnątrz okna
import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Label 1", bg="red")
label1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
#side określa gdzie ma być
#expand - czy ma się rozszerzać na dowolną przestrzeń
#fill - czy windzet wypelni dodatkową przestrzeń czy zajmie minimalną - X, Y, BOTH

label2 = tk.Label(window, text="Label 2", bg="silver")
label2.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

button1 = tk.Button(window, bg="red", text="Button 1")
button1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

button2 = tk.Button(window, bg="yellow", text="Button 2")
button2.pack(side=tk.RIGHT, expand=True, fill=tk.Y)


window.mainloop()