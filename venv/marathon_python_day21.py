# import whole module
import random
print(random.randint(0, 9))
print(random.randrange(0, 10))

# import specific functions
from random import randint, randrange
print(randint(0, 10))
print(randrange(0, 10))

# import all functions
from random import *
print(randint(0, 10))
print(randrange(0, 10))

# give module an alias name
import random as rand
print(rand.randint(0, 9))
print(rand.randrange(0, 10))

# give module function an alias name
from random import randint as rint
print(rint(0, 9))

# import external module
import matplotlib.pyplot
line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matplotlib.pyplot.plot(line)
matplotlib.pyplot.show()

# import user-defined module
import marathon_python_day20
print(marathon_python_day20.__name__)

# use user-defined module
from marathon_python_day20 import fact_data, TestGenerator, CreateTestPool
# create a test pool
test_pool = []
for fact in fact_data:
    fact_obj = CreateTestPool(fact["question"], fact["answer"])
    test_pool.append(fact_obj)

# do fact test
fact_test = TestGenerator(test_pool)

while fact_test.is_last_questions():
    fact_test.generate_next_question()

# comments
print(f"你的總分: {fact_test.score}/{fact_test.question_number}.")

if fact_test.get_score() > 4:
    print("恭喜你答得比黑猩猩好！")
elif fact_test.get_score() == 4:
    print("黑猩猩4ni?")
else:
    print("趕快買本書來看吧！")
