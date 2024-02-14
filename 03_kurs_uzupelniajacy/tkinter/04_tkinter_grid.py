#umieszcza elementy w dwuwymiarowej tabeli - dowolna liczba kolumn i wierszy
import tkinter as tk

window = tk.Tk()

b1 = tk.Button(window, bg="red", text="button 1")
b1.grid(row=0, column=0, ipadx=5, ipady=5)
#pierwszy wiersz, pierwsza kolumna, ipad - dopełnienie wewnątrz

b2 = tk.Button(window, bg="yellow", text="button 2")
b2.grid(row=0, column=1, ipadx=5, ipady=5)
#wiersz pierwszy, columna, druga

b3 = tk.Button(window, bg="pink", text="button 3")
b3.grid(row=0, column=2, ipadx=5, ipady=5)
#wiersz pierwszy, columna trzecia

b4 = tk.Button(window, bg="blue", text="button 4")
b4.grid(row=1, column=0, ipadx=5, ipady=5)
#wiersz drugi, kolumna pierwsza

b5 = tk.Button(window, bg="orange", text="button 5")
b5.grid(row=1, column=1, ipadx=5, ipady=5)
#wiersz drugi, kolumna druga

b6 = tk.Button(window, bg="silver", text="button 6")
b6.grid(row=1, column=2, ipadx=5, ipady=5)
#wiersz drugi, kolumna trzecia

b7 = tk.Button(window, bg="white", text="button 7")
b7.grid(row=2, column=0, columnspan=3, sticky="EW", ipadx=5, ipady=5)
#columnspan - rozszerzy się na trzy kolumny
#sticky - na które strony ma się rozszerzyć widzet jeżeli ma więcej miejsca - NORTH, SOUTH, EAST, WEST


window.mainloop()