# import random module
import random

# random seed
for i in range(5):
    random.seed(1)
    rand_int = random.randint(1, 10)
    print(f"loop {i}: {rand_int}")

# save current state of the generator
rand_state = random.getstate()

# generate random integer
rand_int = random.randint(1, 10)
print(f"Generate a random integer: {rand_int}")

# generate another random integer
rand_int = random.randint(1, 10)
print(f"Generate another random integer: {rand_int}")

# generate random integer after restoring random state
random.setstate(rand_state)
rand_int = random.randint(1, 10)
print(f"Generate a random integer after restoring state: {rand_int}")