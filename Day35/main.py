# modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice, shuffle
import json


# functions
def generate_password():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
    u_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    l_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    password_numbers = [choice(numbers) for _ in range(int(number_combo.get()))]
    password_symbols = [choice(symbols) for _ in range(int(symbol_combo.get()))]
    password_u_letters = [choice(u_letters) for _ in range(int(u_letter_combo.get()))]
    password_l_letters = [choice(l_letters) for _ in range(int(l_letter_combo.get()))]

    password_list = password_numbers + password_symbols + password_u_letters + password_l_letters
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def save_password():

    name = name_entry.get()
    url = url_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(name) == 0 or len(url) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="警告", message="請確認是否有空白欄位！")
    else:
        is_ok = messagebox.askokcancel(title="密碼確認",
                                       message=f"您所輸入的資訊：\n名稱：{name}\n網址：{url}\n帳號：{username}\n密碼：{password}")

        if is_ok:
            new_password_data = {
                name: {
                    "url": url,
                    "username": username,
                    "password": password
                }
            }

            try:
                with open("password_manager.json", "r") as password_file:
                    password_data = json.load(password_file)
            except FileNotFoundError:
                with open("password_manager.json", "w") as password_file:
                    json.dump(new_password_data, password_file, indent=4)
            else:
                password_data.update(new_password_data)
                with open("password_manager.json", "w") as password_file:
                    json.dump(password_data, password_file, indent=4)
            finally:
                name_entry.delete(0, END)
                url_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


def about():
    messagebox.showinfo(title="關於", message="密碼產生器 V1.0")


def search_password():

    name = name_entry.get()
    if len(name) == 0:
        messagebox.showwarning(title="警告", message="請確認名稱是否為空白！")
    else:
        try:
            with open("password_manager.json", "r") as password_file:
                password_data = json.load(password_file)
        except FileNotFoundError:
            messagebox.showwarning(title="警告", message="檔案不存在！")
        else:
            if name in password_data.keys():
                url = password_data[name]["url"]
                username = password_data[name]["username"]
                password = password_data[name]["password"]
                messagebox.showinfo(title="搜尋結果", message=f"名稱：{name}\n網址：{url}\n帳號：{username}\n密碼：{password}")
            else:
                messagebox.showinfo(title="搜尋結果", message=f"此名稱資料不存在！")


# window
password_gen_window = Tk()
password_gen_window.title("密碼產生器")
password_gen_window.config(padx=20, pady=20)

# labels
name_label = Label(text="名稱：")
name_label.grid(row=0, column=0)

url_label = Label(text="網址：")
url_label.grid(row=1, column=0)

username_label = Label(text="帳號：")
username_label.grid(row=2, column=0)

password_label = Label(text="密碼：")
password_label.grid(row=3, column=0)

u_letter_label = Label(text="大寫")
u_letter_label.grid(row=4, column=0, pady=4)

l_letter_label = Label(text="小寫")
l_letter_label.grid(row=4, column=2, pady=4)

number_label = Label(text="數字")
number_label.grid(row=4, column=4, pady=4)

symbol_label = Label(text="符號")
symbol_label.grid(row=4, column=6, pady=4)

# entries
name_entry = Entry(width=34)
name_entry.grid(row=0, column=1, columnspan=5, sticky=W)
name_entry.focus()

url_entry = Entry(width=48)
url_entry.grid(row=1, column=1, columnspan=7)

username_entry = Entry(width=48)
username_entry.grid(row=2, column=1, columnspan=7)

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1, columnspan=5, sticky=W)

# button
generate_password_button = Button(text="產生密碼", width=12, command=generate_password)
generate_password_button.grid(row=3, column=6, columnspan=2, sticky=E)

search_password_button = Button(text="搜尋", width=12, command=search_password)
search_password_button.grid(row=0, column=6, columnspan=2, sticky=E)

# combobox
u_letter_combo = ttk.Combobox(values=[0, 1, 2, 3, 4, 5, 6, 7, 8], width=4)
u_letter_combo.grid(row=4, column=1, pady=4)
u_letter_combo.current(4)

l_letter_combo = ttk.Combobox(values=[0, 1, 2, 3, 4, 5, 6, 7, 8], width=4)
l_letter_combo.grid(row=4, column=3, pady=4)
l_letter_combo.current(4)

number_combo = ttk.Combobox(values=[0, 1, 2, 3, 4, 5, 6, 7, 8], width=4)
number_combo.grid(row=4, column=5, pady=4)
number_combo.current(2)

symbol_combo = ttk.Combobox(values=[0, 1, 2, 3, 4, 5, 6, 7, 8], width=4)
symbol_combo.grid(row=4, column=7, pady=4)
symbol_combo.current(2)

# menus
password_gen_menu = Menu()
password_gen_window.config(menu=password_gen_menu)

file_menu = Menu(tearoff=False)
file_menu.add_command(label="儲存密碼", command=save_password)
file_menu.add_command(label="結束", command=password_gen_window.destroy)

about_menu = Menu(tearoff=False)
about_menu.add_command(label="關於", command=about)

password_gen_menu.add_cascade(label="檔案", menu=file_menu)
password_gen_menu.add_cascade(label="幫助", menu=about_menu)

# mainloop
password_gen_window.mainloop()
