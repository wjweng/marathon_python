import os

# 讀取檔案
file = open("readme.txt", mode='r', encoding="utf-8")
data = file.read()
print(data)
file.close()

# 使用with讀取檔案
with open("readme.txt", mode='r', encoding="utf-8") as file:
    data = file.read()
    print(data)

# 逐行讀取
with open("readme.txt", mode='r', encoding="utf-8") as file:
    for line in file:
        print(line)

# 逐行讀取
with open("readme.txt", mode='r', encoding="utf-8") as file:
    data_list = file.readlines()
    print(data_list)

for line in data_list:
    print(line.rstrip())

# 寫入檔案
with open("record.txt", mode='w', encoding="utf-8") as file:
    file.write("檔案寫入範例\n")

# 附加檔案
with open("record.txt", mode='a', encoding="utf-8") as file:
    file.write("附加檔案範例\n")

# 取得目前的工作目錄
print(os.getcwd())

# 取得絕對路徑
print(os.path.abspath("main.py"))

# 取得相對路徑
print(os.path.relpath("c:\\"))

# 檢查路徑
print(os.path.exists("snake/scoreboard.py"))
print(os.path.exists("snake/highest_score.txt"))
