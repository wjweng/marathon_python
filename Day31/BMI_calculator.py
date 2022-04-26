from tkinter import *


# function
def bmi_button_clicked():
    # calculate BMI
    weight = int(BMI_entry_weight.get())
    height = int(BMI_entry_height.get())

    if height == 0:
        bmi = 0
    else:
        bmi = round(weight / (height / 100) ** 2, 1)

    # BMI interpretation
    if bmi == 0:
        BMI_label_bmi_out.config(text=f"{bmi}")
        BMI_label_category_out.config(text="Error!")
    elif bmi < 18.5:
        BMI_label_bmi_out.config(text=f"{bmi}")
        BMI_label_category_out.config(text="Underweight")
    elif bmi < 24:
        BMI_label_bmi_out.config(text=f"{bmi}")
        BMI_label_category_out.config(text=f"Normal Weight")
    elif bmi < 28:
        BMI_label_bmi_out.config(text=f"{bmi}")
        BMI_label_category_out.config(text="Overweight")
    else:
        BMI_label_bmi_out.config(text=f"{bmi}")
        BMI_label_category_out.config(text=f"Obese")


# window
BMI_window = Tk()
BMI_window.title("BMI calculator")
BMI_window.minsize(width=300, height=200)
BMI_window.config(padx=20, pady=20)

# label
BMI_label_title = Label(width=28, text="BMI calculator", bg="lightyellow", font=("Arial", 12, "normal"))
BMI_label_title.grid(row=0, column=0, columnspan=2, ipadx=2, ipady=2)

BMI_label_height = Label(width=15, text="Height (cm)", bg="yellow", font=("Arial", 10, "normal"))
BMI_label_height.grid(row=1, column=0, padx=5, pady=5)

BMI_label_weight = Label(width=15, text="Weight (kg)", bg="lightgreen", font=("Arial", 10, "normal"))
BMI_label_weight.grid(row=2, column=0, padx=5, pady=5)

BMI_label_bmi = Label(text="BMI：", font=("Arial", 12, "bold"))
BMI_label_bmi.grid(row=4, column=0, padx=5, pady=5)

BMI_label_bmi_out = Label(font=("Arial", 12, "normal"))
BMI_label_bmi_out.grid(row=4, column=1, padx=5, pady=5)

BMI_label_category = Label(text="Category：", font=("Arial", 12, "bold"))
BMI_label_category.grid(row=5, column=0, padx=5, pady=5)

BMI_label_category_out = Label(font=("Arial", 12, "normal"))
BMI_label_category_out.grid(row=5, column=1, padx=5, pady=5)

# entry
BMI_entry_height = Entry(width=20)
BMI_entry_height.grid(row=1, column=1, padx=5, pady=5)

BMI_entry_weight = Entry(width=20)
BMI_entry_weight.grid(row=2, column=1)

# button
BMI_button = Button(width=20, text="Calculate", command=bmi_button_clicked, font=("Arial", 10, "normal"))
BMI_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

BMI_window.mainloop()
