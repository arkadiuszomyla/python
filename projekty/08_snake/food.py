from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()  #nie chcemy nic malować
        self.speed(0) #animacja przemieszczenia będzie wyłączona
        self.refresh()

    def refresh(self):
        shape = random.choice(["square", "circle", "triangle"])  #kształt
        color = random.choice(["blue", "silver", "orange"])      #kolor
        self.hideturtle()
        self.shape(shape)
        self.color(color)
        self.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.showturtle()