# for loop
for i in range(10):
    print(i, end=" ")

print()

# while loop
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

print()

# while loop
principal = 10000
year = 0
interest_rate = 0.01

while principal < 20000:
    principal = principal * (1 + interest_rate)
    year += 1

print(year)

# while loop
input_chr = ""
while input_chr != "q":
    input_chr = input("輸入q結束：")

# while loop for multiplication table
i = j = 1
while i < 10:
    while j < 10:
        print("%d*%d=%-4d" % (i, j, i * j), end=" ")
        j += 1
    i += 1
    j = 1
    print()

# infinite loop
# while True:
    # Do something

# infinite while loop + break
input_chr = ""
while True:
    input_chr = input("輸入q結束：")
    if input_chr == "q":
        break

# while loop + continue
i = 0
odd_list = []
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    odd_list.append(i)
print(odd_list)

# while loop + else
i = 0
odd_list = []
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    odd_list.append(i)
else:
    print(f"End of counting odd numbers to {i-1}")
print(odd_list)
