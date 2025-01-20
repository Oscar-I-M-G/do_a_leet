## this python script automatically uploads my code to github
from tkinter import *
from tkinter import ttk


def send_data():
    print("working")


main_window = Tk()
## putting our title
main_window.title("Do a leet")

main_window.geometry("400x400")
for i in range(16):
    main_window.grid_rowconfigure(i, weight=1)
## configuring columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)


## for the leetcode number title
leetcode_title_var = StringVar()

LeetCode_Number = Label(main_window, text="LeetCode #")
LeetCode_Number.grid(column=0, row=1)  ## this is the position

LeetCode_Number_field = Entry(main_window)
LeetCode_Number_field.grid(column=1, row=1)  ## position

## drop down for languages used
language_used_var = StringVar()
language_used = ttk.Combobox(main_window, width=5, textvariable=language_used_var)
## adding the values
language_used["values"] = ("C", "C++", "Swift", "Python")
language_used.grid(column=0, row=2, columnspan=2)
## setting the default
language_used.current(0)


## Giant text entry box for the code
code_var = StringVar()
code_inserted_label = Label(main_window, text="Code:")
code_inserted_label.grid(column=0, row=3, columnspan=2)

code_inserted = Text(main_window, width=30)
code_inserted.grid(column=0, row=4, columnspan=2, rowspan=10, sticky="nsew")

## Button to send the data
button = Button(main_window, text="Send", command=send_data)
button.grid(row=16, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)

main_window.mainloop()
