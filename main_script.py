## this is my main script for my program

## it will retrieve the data from the form
## if its missing any errors it will contact the ui interface for it to display the errors

import ui_interface as ui


def retrieve(title_, language_, code_):
    print("working")
    title = title_.get()
    language = language_.get()
    code = code_.get("1.0", "end-1c")
    print(f"{title}\n{language}\n{code}")


def main():
    ui.create_ui(retrieve)


if __name__ == "__main__":
    main()
