from turtle import Turtle

WALL_COLOR = "BlueViolet"
WALL_PEN_SIZE = 10

class Wall(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.hideturtle()
        self.pensize(WALL_PEN_SIZE)
        self.color(WALL_COLOR)
        self.speed("fastest")
        self.screen_width = width
        self.screen_height = height
        self.draw()

    def draw(self):
        self.penup()
        self.goto(-(self.screen_width / 2 - 25), self.screen_height / 2 - 45)
        self.pendown()
        self.forward(self.screen_width - 50)
        self.setheading(270)
        self.forward(self.screen_height - 70)
        self.setheading(180)
        self.forward(self.screen_width - 50)
        self.setheading(90)
        self.forward(self.screen_width - 70)