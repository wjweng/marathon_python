# import random module
import random

cities = ["台北", "桃園", "新竹", "台中", "台南"]

# without for loop
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])
print(cities[4])

# with for loop
for city in cities:
    print(city)

# range with 1 parameter
for number in range(5):
    print(number, end=" ")

print("")

# range with 2 parameter
for number in range(6, 11):
    print(number, end=" ")

print("")

# range with 3 parameter
for number in range(0, 11, 2):
    print(number, end=" ")

print("")

# 1 + 2 + ... + 100
sum = 0
for number in range(1, 101):
    sum += number
print(sum)
