# label - windzet, pole okna

import tkinter as tk
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

window = tk.Tk() #uchwyt do okna
window.title("Application")  #nazwa belki
logo = tk.PhotoImage(file="photo.png")  #obraz wczytujemy po otwarciu okna

label1 = tk.Label(window,               #nowa etykieta
                  text = "Hello World!",
                  foreground="white",       #kolor tekstu
                  background="black",       #kolor tła
                  width=20,                 #szerokość wyrażana w ilości znaków
                  height=3,                 #wysokość wyrażana w ilości linii
                  cursor="dot",             #pokazany kurson po najechaniu na label
                  font="Times 18 bold italic underline",
                  anchor=tk.W,              #wyśrodkowanie od kierunków świata lub CENTER (ciągnie z tk)
                  padx=5,                   #dopełnienie, aby tekst nie stykał się z krawędzią, piksele
                  pady=5
                  )
label1.pack()    #wywolujemy etykiete

label2 = tk.Label(window, text = "Hello Again!")
label2.pack()

label3 = tk.Label(window,
                  text="test",   #można ale nie trzeba
                  compound=tk.CENTER,  #bez tego nie będzie działał obraz + tekst
                  foreground="red",
                  image=logo,
                  width=1000,
                  height=1000)
label3.pack()

label3.config(text="test2") #w każdej chwili można zmienić dowolną wartość

window.mainloop()  #nieskonczona pętla, aplikacja sie nie zamknie