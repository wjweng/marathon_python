class Student:

    # initialization
    def __init__(self, name):
        # attributes
        self.__name = name
        self.__score = {"Math": 0, "Physics": 0, "Chemistry": 0}
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    # methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # name = property(get_name, set_name)

    def set_score(self, subject, score):
        if subject not in self.__score:
            self.__add_subject(subject)
        self.__score[subject] = score

    def get_score(self, subject):
        if subject in self.__score:
            print(self.__score[subject])

    def get_subject(self):
        for key in self.__score:
            print(key)

    def __add_subject(self, subject):
        self.__score[subject] = 0

# create an object
student = Student("Jack")

# try to access private attribute
# print(student.__name)

# print name via public method
student.set_name("Rose")
print(student.get_name())

# print name via property
student.name = "Jack"
print(student.name)

# print dictionary of object attributes
print(student.__dict__)

# access private attribute
print(student._Student__name)

# add a subject
# student.__add_subject("Art")

# register a score of a new subject
student.set_score("Art", 80)

# get score of a subject
student.get_score("Art")

# access private method
student._Student__add_subject("Music")

# get all subjects
student.get_subject()
