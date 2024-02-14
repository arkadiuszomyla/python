import turtle
import random

t = turtle.Turtle()

t.forward(100)
t.right(45)
t.fd(50)
t.left(90)
t.backward(50)
t.penup()

t.goto(0, 0) #wracamy na poczatek
t.pendown() #przemiesci sie bez rysowania

for i in range(20):
    t.color(random.choice(["red", "yellow", "blue", "orange"]))
    t.width(i+1)     #ustawiamy grubosc linii
    t.fd(70 + 20 * i) #przesuwa o tyle
    t.right(90)   #skrecamy o 90 stopni


turtle.mainloop()  # bez tego zamknie sie aplikacja



'''
import turtle: Importuje moduł turtle.
turtle.Turtle(): Tworzy nowego żółwia.
forward(distance): Przesuwa żółwia do przodu o określoną odległość.
backward(distance): Przesuwa żółwia do tyłu o określoną odległość.
right(angle): Obraca żółwia w prawo o określony kąt (w stopniach).
left(angle): Obraca żółwia w lewo o określony kąt (w stopniach).
penup(): Podnosi pióro żółwia, aby przesuwał się bez rysowania.
pendown(): Opuszcza pióro żółwia, aby rysował podczas poruszania się.
color(color_name): Ustawia kolor rysowania żółwia. Na przykład: 'red', 'blue', 'green', itp.
pensize(size): Ustawia rozmiar pióra żółwia.
speed(speed): Ustawia prędkość ruchu żółwia. Możliwe wartości to: 'fastest', 'fast', 'normal', 'slow', 'slowest'.
bgcolor(color_name): Ustawia kolor tła.
begin_fill(): Rozpoczyna wypełnianie obszaru.
end_fill(): Kończy wypełnianie obszaru.
circle(radius): Rysuje okrąg o określonym promieniu.
To tylko kilka podstawowych komend w module turtle. Istnieje wiele innych komend, które pozwalają kontrolować żółwia i tworzyć bardziej zaawansowane rysunki. Możesz znaleźć więcej informacji o module turtle w dokumentacji Pythona lub w różnych tutorialach dostępnych online.
'''