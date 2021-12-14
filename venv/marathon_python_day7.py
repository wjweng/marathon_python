import random

# generate a random integer between 1 and 9
rand_int = random.randrange(1, 10, 1)
print(rand_int)

# generate a random interger between 1 and 9
rand_int = random.randint(1, 9)
print(rand_int)

# generate a random floating point between [0.0, 1.0)
rand_float = random.random()
print(rand_float)

# generate a random floating point corresponding to an uniform distribution between [0, 1]
rand_float = random.uniform(0, 1)
print(rand_float)

# generate a random floating point corresponding to a exponential distribution with lambda = 0.1
rand_float = random.expovariate(0.1)
print(rand_float)

# generate a random floating point corresponding to a gaussian distribution with mean = 0 and standard deviation = 1
rand_float = random.gauss(0, 1)
print(rand_float)

# generate a random floating point corresponding to a normal distribution with mean = 0 and standard deviation = 1
rand_float = random.normalvariate(0, 1)
print(rand_float)

# random list
cities = ["台北", "桃園", "新竹", "台中", "台南"]
random.shuffle(cities)
print(cities)

# random item from a list
rand_city = random.choice(cities)
print(rand_city)

# random items from a list
rand_city = random.choices(cities, [10, 20, 30, 40, 50], k=2)
print(rand_city)

# random sample from a list
rand_city = random.sample(cities, 2)
print(rand_city)
