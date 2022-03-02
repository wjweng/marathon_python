# # create a student
# student1_name = "Jack"
# student1_score = {"Math": 0, "Physics": 0, "Chemistry": 0}
#
# # register a score of a subject
# if "Math" in student1_score:
#     student1_score["Math"] = 80
#
# # get a score of a subject
# if "Math" in student1_score:
#     print(student1_score["Math"])
#
# # add a subject
# if "Art" not in student1_score:
#     student1_score["Art"] = 0
#
# # create another student
# student2_name = "Rose"
# student2_score = {"Math": 0, "Physics": 0, "Chemistry": 0}
#
# # for test
# print(student1_score)
# print(student2_score)

# create a class
class Student:

    # class attribute
    classname = "My Class"

    # initialization
    def __init__(self, name):
        # instance attribute
        self.name = name
        self.score = {"Math": 0, "Physics": 0, "Chemistry": 0}

    # methods
    def set_score(self, subject, score):
        if subject in self.score:
            self.score[subject] = score

    def get_score(self, subject):
        if subject in self.score:
            print(self.score[subject])

    def get_subject(self):
        for key in self.score:
            print(key)

    def add_subject(self, subject):
        if subject not in self.score:
            self.score[subject] = 0

# access class attribute
print(Student.classname)

# create objects
student_1 = Student("Jack")
student_2 = Student("Rose")

print(student_1.name)
print(student_2.name)

# register a score of a subject
student_1.set_score("Math", 80)
student_2.set_score("Physics", 90)

# get score of a subject
student_1.get_score("Math")
student_2.get_score("Physics")

# add a subject
student_1.add_subject("Art")
student_2.add_subject("Music")

# get all subject
student_1.get_subject()
student_2.get_subject()

# modify class attribute
Student.classname = "Jack's Class"
print(Student.classname)
print(student_1.classname)
