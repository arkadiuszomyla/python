import tkinter as tk


window = tk.Tk()

def buttonClicked():
    print("clicked!")
    quit()    #kończy program


button = tk.Button(
    window,
    text="QUIT",
    bd=10,    #szerokość w pikselach obramowania przycisku
    fg="red",
    bg="green",
    activeforeground="black",
    activebackground="silver",
    font="Times 18 bold",
    height=3,      #trzy linie tekstu
    width=20,      #20 znaków
    padx=10,       #dopełnienie horyzontalne i wertykalne(y) od każdej strony
    pady=10,
    relief="groove",        #styl obramowania
    command=buttonClicked   #funkcja wywołana kiedy zostanie kliknięte
)

button.pack()

window.mainloop()