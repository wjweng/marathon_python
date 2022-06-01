# FileNotFoundError
# with open("file.txt", "r") as file:
#     file.read()

# KeyError
# dictionary = {"台北市": 100}
# value = dictionary["新北市"]

# IndexError
# city_list = ["台北市", "新北市", "台中市"]
# city = city_list[3]

# TypeError
# text = "大家好"
# print(text + 1)

# try - except
# def print_city(index):
#     city_list = ["台北市", "新北市", "台中市"]
#
#     try:
#         city = city_list[index]
#     except IndexError:
#         print("索引值超出範圍！")
#
# print_city(3)

# try - except - else
# def print_city(index):
#     city_list = ["台北市", "新北市", "台中市"]
#
#     try:
#         city = city_list[index]
#     except IndexError:
#         print("索引值超出範圍！")
#     else:
#         print(city)
#
# print_city(0)

# try...except...else...finally
# def print_city(index):
#     city_list = ["台北市", "新北市", "台中市"]
#
#     try:
#         city = city_list[index]
#     except IndexError:
#         print("索引值超出範圍！")
#     else:
#         print(city)
#     finally:
#         print("執行完畢！")
#
# print_city(0)

# 捕捉多個異常
# def print_city(index):
#     city_list = ["台北市", "新北市", "台中市"]
#
#     try:
#         city = city_list[index]
#     except IndexError:
#         print("索引值超出範圍！")
#     except TypeError:
#         print("型別錯誤！")
#     else:
#         print(city)
#     finally:
#         print("執行完畢！")
#
# print_city(3)
# print_city("a")

# 捕捉多個異常
# def print_city(index):
#     city_list = ["台北市", "新北市", "台中市"]
#
#     try:
#         city = city_list[index]
#     except (IndexError, TypeError):
#         print("索引值超出範圍 或 型別錯誤！")
#     else:
#         print(city)
#     finally:
#         print("執行完畢！")
#
# print_city(3)
# print_city("a")

# 使用內建錯誤訊息
# def print_city(index):
#     city_list = ["台北市", "新北市", "台中市"]
#
#     try:
#         city = city_list[index]
#     except (IndexError, TypeError) as error_message:
#         print(f"{error_message}")
#     else:
#         print(city)
#     finally:
#         print("執行完畢！")
#
# print_city(3)
# print_city("a")

def print_city(index):
    city_list = ["台北市", "新北市", "台中市"]

    if index > 1:
        raise IndexError("索引值超出自訂範圍")

print_city(2)
