from tkinter import *

window = Tk()
window.title("Hello World!")
window.minsize(width=500, height=500)
# window.geometry("500x500")
# window.config(padx=20, pady=20)
window.resizable(width=False, height=False)
window.config(bg="gold")

# label
label = Label(text="my label", font=("Arial", 14, "bold"), padx=5, pady=5, bg="red", fg="yellow")
label.pack()

# button
def button_clicked():
    label.config(text="Hello World!")

button = Button(text="Click Me", font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="light green", command=button_clicked)
button.pack()

# entry
entry = Entry(width=30, font=("Arial", 14, "bold"), bg="red", fg="yellow", state=NORMAL)
entry.insert(END, string="some text")
entry.pack()
print(entry.get())

# text
text = Text(height=5, width=30, font=("Arial", 14, "bold"), bg="blue", fg="light green", state=NORMAL)
# text.focus()
text.insert(END, "line 1\nline 2\nline 3")
text.pack()
print(text.get("1.0", "2.4"))

# spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, font=("Arial", 14, "bold"), command=spinbox_used, bg="red", fg="yellow", state=NORMAL)
spinbox.pack()

# scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=10, font=("Arial", 14, "bold"), width=15, orient=HORIZONTAL, length=200, command=scale_used)
scale.pack()

# radiobutton
def radiobutton_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radiobutton_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()

# checkbutton
def checkbutton_clicked():
    print(f"Option1: {checked_state1.get()}, Option2: {checked_state2.get()}")

checked_state1 = IntVar()
checked_state2 = IntVar()

checkbutton1 = Checkbutton(text="Option1", variable=checked_state1, command=checkbutton_clicked)
checkbutton2 = Checkbutton(text="Option2", variable=checked_state2, command=checkbutton_clicked)
checkbutton1.pack()
checkbutton2.pack()

# listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

listbox = Listbox(width=15, height=4, selectmode=EXTENDED)
fruit = ["Option1", "Option2", "Option3", "Option4"]
for item in fruit:
    listbox.insert(fruit.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
