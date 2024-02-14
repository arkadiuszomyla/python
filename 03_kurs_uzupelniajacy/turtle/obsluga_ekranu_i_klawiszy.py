import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()


win.title("Aplikacja")
win.bgcolor("yellow")  #kolor wypełnienia
win.setup(width=500, height=550) #rozmiar okna

t.forward(100)
print("x: ", t.xcor())  #podajemy współrzędne
print("y: ", t.ycor())


def keyPressedW():
    print("w clicked")
    t.fd(20)

def keyPressedS():
    print("s clicked")
    t.backward(20)

win.listen()  #nasłuchujemy kliknięcia
win.onkey(keyPressedW, "w")   # funkcja reaguje na klawisz w
win.onkey(keyPressedS, "s")   # funkcja reaguje na klawisz w

win.tracer(0) #my decydujemy kiedy okno ma być odrysowane

# kiedy okno aplikacji ma być odrysowane, mniej zasobów
while True:
    win.update()
    time.sleep(0.1)

win.mainloop()