import sqlite3
import menu


def add_student():
    pass

def _exit():
    return True

def main():
    actions = {
        "Add student": add_student,
        "Exit": _exit
    }

    while True:
        exit_loop = menu.select_action(actions)

        if exit_loop:
            break
    pass

if __name__ == "__main__":
    main()
