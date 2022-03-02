# list
city = ["台北", "桃園", "新竹", "台中", "台南"]
print(city)

student = ["小明", 140, 45]
print(student)

# index
print(student[0])
print(student[1])
print(student[2])
print(student[-1])
print(student[-2])
print(student[-3])

# list slices
print(city[2:5])
print(city[:2])
print(city[2:])
print(city[1:5:2])
print(city[:])

# list modification
student[2] = 50
print(student)

# list concatenation
city = city + ["宜蘭"]
print(city)

city.append(["花蓮", "台東"])
print(city)

city.extend(["澎湖", "金門"])
print(city)

city.insert(4, "嘉義")
print(city)

# list deletion
del city[4]
print(city)

city.pop()
print(city)
city.pop(7)
print(city)

city.remove("宜蘭")
print(city)
