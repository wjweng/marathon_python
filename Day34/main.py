import json

number_list = [2, 4, 6, 8, 10]
number_json = json.dumps(number_list)
number_list_from_json = json.loads(number_json)

print(number_json)
print(type(number_json))
print(number_list_from_json)
print(type(number_list_from_json))

password_dict = {
    "Google": {
        "url": "www.google.com",
        "username": "user",
        "password": "fj;sagjpwej;"
    }
}
password_json = json.dumps(password_dict)
password_list_from_json = json.loads(password_json)

print(password_json)
print(type(password_json))
print(password_list_from_json)
print(type(password_list_from_json))

with open("password.json", "w") as password_file:
    json.dump(password_dict, password_file, indent=4)

with open("password.json", "r") as password_file:
    password_dict_from_json_file = json.load(password_file)

print(password_dict_from_json_file)
print(type(password_dict_from_json_file))
