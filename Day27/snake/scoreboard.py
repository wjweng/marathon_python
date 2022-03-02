from turtle import Turtle
from os import path

SCORE_COLOR = "white"
SCORE_POSITION = (0, 265)
GAMEOVER_COLOR = "dark red"
GAMEOVER_POSITION = (0, -30)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color(SCORE_COLOR)
        self.speed("fastest")
        self.goto(SCORE_POSITION)

        if path.exists("snake/highest_score.txt"):
            with open("snake/highest_score.txt", mode='r') as score_file:
                self.highest_score = int(score_file.read())
        else:
            self.highest_score = 0
        self.write(f"score: {self.score}, highest_score: {self.highest_score}", False, align="center", font=("Arial", 20, "normal"))

    def get_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}, highest_score: {self.highest_score}", False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.color(GAMEOVER_COLOR)
        self.goto(GAMEOVER_POSITION)
        self.write("Game Over", False, align="center", font=("Arial", 40, "normal"))

        if self.score > self.highest_score:
            with open("snake/highest_score.txt", mode='w') as score_file:
                score_file.write(str(self.score))
