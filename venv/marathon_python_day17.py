# global variable
global_message = "This is a global message."

def print_global_message():
    print("In function:", global_message)

print_global_message()
print("In main:", global_message)

# modify global message in function
def modify_global_message():
    global_message = "Modify global message."
    print("In function:", global_message)

modify_global_message()
print("In main:", global_message)

# use global keyword
def modify_global_message():
    global global_message
    global_message = "Modify global message."
    print("In function:", global_message)

modify_global_message()
print("In main:", global_message)

# local variable
# def define_local_message():
#     local_message = "This is a local message."
#
# define_local_message()
# print(local_message)

def print_local_message():
    local_message = "This is a local message."
    def modify_outer_message():
        local_message = "Modify local message."
        print("Inner function:", local_message)
    modify_outer_message()
    print("Outer function:", local_message)

print_local_message()

def print_local_message():
    local_message = "This is a local message."
    def modify_outer_message():
        nonlocal local_message
        local_message = "Modify local message."
        print("Inner function:", local_message)
    modify_outer_message()
    print("Outer function:", local_message)

print_local_message()

def local_variables():
    local_var_a = 1
    local_var_b = 2
    print("Local variables:", locals())

global_var_a = 1
global_var_b = 2
local_variables()
print("Global variables:", globals())
