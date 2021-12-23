# loop through a dictionary
cities_dict = { "台北": 2531659,
                "新北": 4011586,
                "桃園": 2272452,
                "台中": 2814422,
                "台南": 1863435,
                "高雄": 2746939}

for city in cities_dict:
    print(city, end=" ")

print()

# keys() method
for city in cities_dict.keys():
    print(city, end=" ")

print()

# values() method
for population in cities_dict.values():
    print(population, end=" ")

print()

# items() method
for city, population in cities_dict.items():
    print(city, population, end=" ")

print()

for city_pop in cities_dict.items():
    print(city_pop, end=" ")

print()

# dictionaries in a list
city0 = { "name": "台北", "population": 2531659, "area": 271}
city1 = { "name": "新北", "population": 4011586, "area": 2052}
city2 = { "name": "桃園", "population": 2272452, "area": 1220}
city3 = { "name": "台中", "population": 2814422, "area": 2214}
city4 = { "name": "台南", "population": 1863435, "area": 2191}
city5 = { "name": "高雄", "population": 2746939, "area": 2951}
special_municipality_list = [city0, city1, city2, city3, city4, city5]
for city in special_municipality_list:
    print(city)

# lists in a dictionary
countries_dict = { "Asia": ["Japan", "Korea", "Taiwan"],
              "Europe": ["Germany", "France", "Spain"],
              "America": ["USA", "Canada", "Argentina"]}
for continent, country in countries_dict.items():
    print(f"{continent}: {country}")

# dictionaries in a dictionary
cities_dict = { "台北": {"population": 2531659, "area": 271},
                "新北": {"population": 4011586, "area": 2052},
                "桃園": {"population": 2272452, "area": 1220},
                "台中": {"population": 2814422, "area": 2214},
                "台南": {"population": 1863435, "area": 2191},
                "高雄": {"population": 2746939, "area": 2951}}
for city, info in cities_dict.items():
    print(f"{city}: {info}")
