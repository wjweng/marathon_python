# tuple
cities_tuple = ("台北", "新北", "桃園", "台中", "台南", "高雄")
print(cities_tuple)
print(type(cities_tuple))

# tuple with only one element
# without 「,」
one_tuple = ("台北")
print(one_tuple)
print(type(one_tuple))

# with 「,」
one_tuple = ("台北",)
print(one_tuple)
print(type(one_tuple))

# empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

# read tuple
print(cities_tuple[0])
print(cities_tuple[1])
print(cities_tuple[-1])
print(cities_tuple[-2])

# tuple slices
print(cities_tuple[2:5])
print(cities_tuple[:2])
print(cities_tuple[2:])
print(cities_tuple[1:5:2])
print(cities_tuple[:])

# redefine tuple
cities_tuple = ("台北", "新北", "桃園", "台中", "台南", "高雄")
print(cities_tuple)

cities_tuple = ("台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市")
print(cities_tuple)

# list to tuple
cities_list = ["台北", "新北", "桃園", "台中", "台南", "高雄"]
cities_tuple = tuple(cities_list)
print(cities_tuple)

# tuple to list
cities_list = list(cities_tuple)
print(cities_list)

# for loop + tuple
cities_tuple = ("台北", "新北", "桃園", "台中", "台南", "高雄")
for city in cities_tuple:
    print(city, end=" ")

print()

# generator for tuple
scores_tuple = ()
scores_tuple = (x for x in range(10))
print(scores_tuple)

scores_tuple = tuple((x for x in range(10)))
print(scores_tuple)
