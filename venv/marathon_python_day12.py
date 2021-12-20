# define function
def hello():
    print("Hello World!")

hello()

# define function with 1 input parameter
def hello_to_someone(name):
    print(f"Hello {name}!")

hello_to_someone(input("What's your name? "))

# define function with more than one input parameter
def personal_info(name, height, weight):
    print(f"Hello {name}!")
    print(f"Your height is {height}!")
    print(f"Your weight is {weight}!")

info_name = input("What's your name? ")
info_height = input("Height? ")
info_weight = input("Weight? ")
personal_info(name=info_name, weight=info_weight, height=info_height)

# define function with default parameter
def personal_info(name, height, weight, birthplace="Taiwan"):
    print(f"Hello {name}!")
    print(f"Your height is {height}!")
    print(f"Your weight is {weight}!")
    print(f"Your birthplace is {birthplace}")

personal_info(name="小明", height=176, weight=60)
personal_info(name="小華", height=160, weight=55, birthplace="Japan")

# define function with default parameter and returned value
def personal_info(name, height, weight, birthplace="Taiwan"):
    print(f"Hello {name}!")
    print(f"Your height is {height}!")
    print(f"Your weight is {weight}!")
    print(f"Your birthplace is {birthplace}")
    return [name, height, weight, birthplace]

personal_info_list = personal_info(name="小明", height=176, weight=60)
print(personal_info_list)
