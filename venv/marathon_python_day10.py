# import random module
import random

# nested for loop
for i in range(1, 10):
    for j in range (1, 10):
        print("%d*%d=%-4d" % (i, j, i*j), end=" ")
    print()

# break
scores_list = []
for _ in range(10):
    scores_list.append(random.randint(0, 100))
scores_list.sort(reverse=True)

for score in scores_list:
    if score > 60:
        print(score, end=" ")
    else:
        break

print()

# continue
odd_list = []
for i in range(1, 10):
    if i % 2 == 0:
        continue
    odd_list.append(i)
print(odd_list)

print()

# list comprehension
scores_list = []
scores_list = [random.randint(0, 100) for _ in range(10)]
print(scores_list)

odd_list = []
odd_list = [i for i in range(1, 10) if i % 2 == 1]
print(odd_list)

add_to_10 = []
add_to_10 = [[i, j] for i in range(1, 10) for j in range(1, 10) if i + j == 10]
print(add_to_10)
