## this is my main script for my program

## it will retrieve the data from the form
## if its missing any errors it will contact the ui interface for it to display the errors

import ui_interface as ui


def retrieve(title_, language_, code_):
    flag = False
    error_message_var_title = ""
    error_message_var_code = ""
    print("working")
    title = title_.get()
    language = language_.get()
    code = code_.get("1.0", "end-1c")
    ##displaying error messages
    ## leetcode title must be a number:
    if not title.isdigit():
        error_message_var_title = "Must be a integer"
        flag = True
    elif title == "":
        error_message_var_title = "Cannot be empty, Must be a number"
        flag = True
    ## check if code is different tha null
    if code.strip() == "":
        error_message_var_code = "Where is the code man?"
        flag = True
        
    if flag:
        ui.error_message_title.config(text=error_message_var_title)
        ui.error_message_code.config(text=error_message_var_code)
        return
    ##print(f"{title}\n{language}\n{code}")
    return title, language, code

## creating files
def create_file(filename, content):
    return




def main():
    ui.create_ui(retrieve)


if __name__ == "__main__":
    main()
