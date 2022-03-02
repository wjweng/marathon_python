from turtle import Turtle

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
        self.write(f"score: {self.score}", False, align="center", font=("Arial", 20, "normal"))

    def get_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.color(GAMEOVER_COLOR)
        self.goto(GAMEOVER_POSITION)
        self.write("Game Over", False, align="center", font=("Arial", 40, "normal"))