# list
cities_list = ["台北", "新北", "桃園", "台中", "台南", "高雄"]
print(cities_list[0])

# dictionary
cities_dict = {"台北": 2531659, "新北": 4011586, "桃園": 2272452, "台中": 2814422, "台南": 1863435, "高雄": 2746939}
print(cities_dict)
print(cities_dict["台北"])

# modify dictionary
cities_dict["台北"] = 2530000
print(cities_dict)

cities_dict["新竹"] = 452665
print(cities_dict)

del cities_dict["新竹"]
print(cities_dict)

del_key = cities_dict.pop("高雄")
print(del_key)
print(cities_dict)
