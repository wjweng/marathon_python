from turtle import Turtle, Screen

# 建立畫布
screen = Screen()
screen.colormode(255)
screen.bgcolor(0, 255, 0)
screen.title("我的畫布")
screen.setup(600, 600)
screen.clearscreen()

# 建立畫筆
turtle = Turtle()

# 寫字
turtle.hideturtle()
turtle.write("Hello 你好！", move=False, align="center", font=("Arial", 20, "bold"))
turtle.showturtle()
screen.resetscreen()

# 前進、後退
turtle.forward(100)
turtle.backward(100)
screen.resetscreen()

# 移至定點
turtle.penup()
turtle.goto(-200, 200)
turtle.home()
screen.resetscreen()

turtle.setx(-200)
turtle.sety(200)
screen.resetscreen()

# 移動方向
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()

for side in range(3, 11):
    angle = 360 / side
    for _ in range(side):
        turtle.forward(100)
        turtle.right(angle)
screen.resetscreen()

# 填充顏色
screen.colormode(255)
turtle.fillcolor(0, 255, 0)

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()

turtle.begin_fill()
for _ in range(5):
    turtle.forward(100)
    turtle.left(144)
turtle.end_fill()
screen.resetscreen()

turtle.hideturtle()

# 烏龜賽跑
import random
import time

turtle_list = []
turtle_color_list = ["green", "blue", "red", "yellow", "purple"]
turtle_start_x = -280
turtle_start_y = -200

for player in range(5):
    turtle = Turtle(shape="turtle", visible=False)
    turtle.color(turtle_color_list[player])
    turtle.penup()
    turtle.goto(turtle_start_x, turtle_start_y)
    turtle.showturtle()
    turtle_list.append(turtle)
    turtle_start_y += 100

time.sleep(1)
is_race_on = True
while is_race_on:
    time.sleep(0.04)
    player = random.randint(0, 4)
    turtle_list[player].forward(10)
    if turtle_list[player].xcor() > 260:
        is_race_on = False

screen.exitonclick()
