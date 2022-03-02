import random
from turtle import Turtle

FOOD_SHAPE = "circle"
FOOD_COLOR = "gold"
ALIGNMENT_FACTOR = 20

class Food(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.screen_width = width
        self.screen_height = height
        self.random_food()

    def random_food(self):
        random_x = random.randint(-(self.screen_width / 2 - 40), (self.screen_width / 2 - 40))
        random_x = ALIGNMENT_FACTOR * round(random_x / ALIGNMENT_FACTOR)
        random_y = random.randint(-(self.screen_height / 2 - 40), (self.screen_width / 2 - 60))
        random_y = ALIGNMENT_FACTOR * round(random_y / ALIGNMENT_FACTOR)
        self.goto(random_x, random_y)