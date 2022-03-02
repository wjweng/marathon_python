# 主程式
import time
from turtle import Screen
from snake.snake import Snake
from snake.wall import Wall
from snake.food import Food
from snake.scoreboard import Scoreboard

# 遊戲參數
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "貪食蛇"

# 建立Screen物件
snake_screen = Screen()

# 遊戲畫面設定
snake_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
snake_screen.bgcolor(SCREEN_COLOR)
snake_screen.title(SCREEN_TITLE)
snake_screen.tracer(0)

# 遊戲難度
level = snake_screen.textinput(title="貪食蛇-遊戲難度", prompt="請選擇遊戲難度：1(簡單) ~ 9(困難)")
time_delay = (10 - float(level)) * 0.05

# 建立遊戲相關物件
snake = Snake()
wall = Wall(SCREEN_WIDTH, SCREEN_HEIGHT)
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = Scoreboard()

# 按鍵設定
snake_screen.listen()
snake_screen.onkeypress(snake.move_up, "Up")
snake_screen.onkeypress(snake.move_down, "Down")
snake_screen.onkeypress(snake.turn_left, "Left")
snake_screen.onkeypress(snake.turn_right, "Right")

# 遊戲主程式
is_game_on = True
while is_game_on:
    # 遊戲畫面更新
    snake_screen.update()
    time.sleep(time_delay)
    snake.move()

    # 是否吃到食物
    if snake.is_collision_with_food(food):
        food.random_food()
        snake.extend_snake()
        scoreboard.get_score()

    # 是否撞牆
    if snake.is_collision_with_wall(width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        is_game_on = False
        scoreboard.game_over()

    # 是否撞身體
    if snake.is_collision_with_body():
        is_game_on = False
        scoreboard.game_over()

# 畫面暫停
snake_screen.exitonclick()
