## this python script automatically uploads my code to github
from tkinter import *
from tkinter import ttk


def validate_integer(P):
    return P.isdigit() or P == ""


def create_ui(on_clicky):
    main_window = Tk()
    ## putting our title
    main_window.title("Do a leet")

    main_window.geometry("500x500")
    for i in range(16):
        main_window.grid_rowconfigure(i, weight=1)
    ## configuring columns
    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=1)

    ## for the leetcode number title

    LeetCode_Number = Label(main_window, text="LeetCode #")
    LeetCode_Number.grid(column=0, row=1)  ## this is the position
    ## to validate number
    validate_input = (main_window.register(validate_integer), '%P')
    LeetCode_Number_field = Entry(main_window, validate='key', validatecommand=validate_input)
    LeetCode_Number_field.grid(column=1, row=1)  ## position
    
    ## Error message for the number title
    global error_message_title
    error_message_title = Label(main_window, text="", fg="red")
    error_message_title.grid(column=1, row=2, columnspan=2)
    

    ## drop down for languages used
    language_used = ttk.Combobox(main_window, width=5)
    ## adding the values
    language_used["values"] = ("C", "C++","Java","Swift", "Python")
    language_used.grid(column=0, row=3, columnspan=2)
    ## setting the default
    language_used.current(0)

    
    ## Giant text entry box for the code
    
    ## Error message
    global error_message_code
    error_message_code = Label(main_window, text="" , fg="red")
    error_message_code.grid(column=0, row=4)
    
    code_inserted_label = Label(main_window, text="Code:")
    code_inserted_label.grid(column=0, row=5, columnspan=2)

    code_inserted = Text(main_window, width=30)
    code_inserted.grid(column=0, row=6, columnspan=2, rowspan=8, sticky="nsew")

    ## Button to send the data
    button = Button(
        main_window,
        text="Send",
        command=lambda: on_clicky(LeetCode_Number_field, language_used, code_inserted),
    )
    button.grid(row=15, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)

    main_window.mainloop()
