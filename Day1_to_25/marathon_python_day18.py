# create a set by {}
cities_set = {"台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市"}
print(cities_set)
print(type(cities_set))

# duplicate element
cities_set = {"台北市", "新北市", "新北市", "桃園市", "台中市", "台南市", "高雄市"}
print(cities_set)

# create a set by set()
str_set = set("This is my marathon Python challenge.")
print(str_set)

list_set = set(["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市"])
print(list_set)

dict_set = set({"台北市": 2531659, "新北市": 4011586, "桃園市": 2272452, "台中市": 2814422, "台南市": 1863435, "高雄市": 2746939})
print(dict_set)

tuple_set = set(("台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市"))
print(tuple_set)

empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

# add or remove elements in a set
cities_set.add("新竹市")
print(cities_set)

cities_set.remove("新竹市")
print(cities_set)

# union
A_set = {3, 6, 9, 12, 15}
B_set = {5, 10, 15}
AB_union = A_set | B_set
print(AB_union)

# intersection
A_set = {3, 6, 9, 12, 15}
B_set = {5, 10, 15}
AB_intersection = A_set & B_set
print(AB_intersection)

# difference
A_set = {3, 6, 9, 12, 15}
B_set = {5, 10, 15}
AB_difference = A_set - B_set
print(AB_difference)

# symmetric difference
A_set = {3, 6, 9, 12, 15}
B_set = {5, 10, 15}
AB_sym_difference = A_set ^ B_set
print(AB_sym_difference)

# subset and superset
A_set = {3, 6, 9, 12, 15}
B_set = {3, 5, 6, 9, 10, 12, 15}
print(f"Is A_set a subset of B_set? {A_set.issubset(B_set)}")
print(f"Is B_set a superset of A_set? {B_set.issuperset(A_set)}")

# same set
A_set = {3, 6, 9, 12, 15}
B_set = {3, 5, 6, 9, 10, 12, 15}
C_set = {3, 6, 9, 12, 15}
print(f"Is A_set the same as B_set? {A_set == B_set}")
print(f"Is A_set the same as C_set? {A_set == C_set}")

# loop for set
for city in cities_set:
    print(city, end=" ")

print()

# set generator
A_set = {num for num in range(1, 16) if num % 3 == 0}
print(A_set)
