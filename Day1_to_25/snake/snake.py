from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.move_angle_list = []

    def create_snake(self):
        for position in START_POSITION:
            self.add_snake_body(position)

    def extend_snake(self):
        self.add_snake_body(self.snake_body[-1].position())

    def add_snake_body(self, position):
        body_seg = Turtle(shape="square")
        body_seg.color("Green")
        body_seg.penup()
        body_seg.goto(position)
        self.snake_body.append(body_seg)

    def move(self):
        # 檢查是否要轉彎
        while self.move_angle_list:
            next_move_angle = self.move_angle_list.pop(0)
            if next_move_angle != self.head.heading() and \
               next_move_angle != (self.head.heading() + 180) % 360:
                self.head.setheading(next_move_angle)
                break;
            else:
                continue;

        # 往前移動
        for body_seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_seg - 1].xcor()
            new_y = self.snake_body[body_seg - 1].ycor()
            self.snake_body[body_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        self.move_angle_list.append(90)

    def move_down(self):
        self.move_angle_list.append(270)

    def turn_right(self):
        self.move_angle_list.append(0)

    def turn_left(self):
        self.move_angle_list.append(180)

    def is_collision_with_food(self, food):
        if self.head.distance(food) < 5:
            return True
        return False

    def is_collision_with_wall(self, width, height):
        if self.head.xcor() > (width / 2 - 30) or \
           self.head.xcor() < -(width / 2 - 30) or \
           self.head.ycor() > (height / 2 - 50) or \
           self.head.ycor() < -(height / 2 - 30):
            return True
        return False

    def is_collision_with_body(self):
        for body_seg in self.snake_body[1:]:
            if self.head.distance(body_seg) < 5:
                return True
        return False