from tkinter import *

window1 = Tk()
window1.title("視窗元件配置")
window1.minsize(width=300, height=50)

label11 = Label(window1, text="label 1", bg="lightyellow")
label12 = Label(window1, text="label 2", bg="yellow")
label13 = Label(window1, text="label 3", bg="lightgreen")

label11.pack(side=LEFT, ipadx=10)
label12.pack(side=LEFT, ipadx=10)
label13.pack(side=LEFT, ipadx=10, fill="both", expand=True)

window2 = Tk()
window2.title("視窗元件配置2")
window2.geometry("300x100")

label21 = Label(window2, text="label 1", bg="lightyellow")
label22 = Label(window2, text="label 2", bg="yellow")
label23 = Label(window2, text="label 3", bg="lightgreen")

label21.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.2)
label22.place(relx=0.4, rely=0.4, relheight=0.3, relwidth=0.2)
label23.place(relx=0.7, rely=0.4, relheight=0.4, relwidth=0.2)

window3 = Tk()
window3.title("視窗元件配置3")
window3.geometry("300x100")

label31 = Label(window3, text="label 1", bg="lightyellow", width=20)
label32 = Label(window3, text="label 2", bg="yellow")
label33 = Label(window3, text="label 3", bg="lightgreen")

entry31 = Entry(window3)
entry32 = Entry(window3)

label31.grid(row=0, column=0, columnspan=2, padx=5, pady=5, ipadx=1, ipady=1)
label32.grid(row=1, column=0, padx=5, pady=5, ipadx=1, ipady=1)
label33.grid(row=2, column=0, padx=5, pady=5, ipadx=1, ipady=1)

entry31.grid(row=1, column=1, padx=5, pady=5, ipadx=1, ipady=1)
entry32.grid(row=2, column=1, padx=5, pady=5, ipadx=1, ipady=1)

window1.mainloop()
window2.mainloop()
window3.mainloop()
