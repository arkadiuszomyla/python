import tkinter as tk

window = tk.Tk()

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=5, width=30, padx=5, pady=5, font="Times 18 bold")

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.config(command=textBox.yview) #łączymy elementy
textBox.config(yscrollcommand=scrollbar.set) #łączymy elementy

textBox.insert(tk.END, "HELLO WORLD \nHELLO AGAIN") #dodajemy tekst na koncu

print("Text data:", textBox.get(1.0, "end")) #wypisujemy tekst od początku do końca

window.mainloop()