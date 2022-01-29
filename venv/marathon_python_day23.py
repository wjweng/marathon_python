class Animal():

    def __init__(self):
        self.class_name = "動物"
        self.eyes_num = 2
        self.legs_num = 4

    def breath(self, animal):
        print(f"{animal}呼吸")

class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.class_name = "小狗"

    def breath(self, dog="小狗"):
        super().breath(dog)

    def eat(self, dog):
        print(f"{dog}吃肉")

    def friend(self):
        print(f"{Bird().class_name}是我的朋友")

class Pet():

    def __init__(self):
        self.class_name = "寵物"

    def eat(self, pet):
        print(f"{pet}吃罐頭")

    def play(self, pet):
        print(f"{pet}玩球")

class Bird(Animal):

    def __init__(self):
        super().__init__()
        self.class_name = "小鳥"
        self.legs_num = 2
        self.wings_num = 2

    def breath(self, bird="小鳥"):
        super().breath(bird)

    def fly(self):
        print(f"{self.class_name}會飛")

    def friend(self):
        print(f"{Dog().class_name}是我的朋友")

class Poodle(Dog, Pet):

    def __init__(self):
        super().__init__()
        self.class_name = "貴賓狗"

    def breath(self):
        super().breath(self.class_name)

    def eat(self):
        super().eat(self.class_name)

    def play(self):
        super().play(self.class_name)

dog = Dog()
print(f"{dog.class_name}有{dog.eyes_num}個眼睛、{dog.legs_num}隻腳")
dog.breath()
dog.friend()

bird = Bird()
print(f"{bird.class_name}有{bird.eyes_num}個眼睛、{bird.legs_num}隻腳、{bird.wings_num}隻翅膀")
bird.breath()
# bird.fly()

poodle = Poodle()
print(f"{poodle.class_name}有{poodle.eyes_num}個眼睛、{poodle.legs_num}隻腳")
poodle.breath()
poodle.eat()
poodle.play()
