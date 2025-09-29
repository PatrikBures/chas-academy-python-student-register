import menu
import sq


def add_student():
    name = ""
    try:
        while not name:
            name = input("Name: ")

        age = menu.select_int_range("Age: ", 0, 1000)
        if age < 0: return

        hobby = input("Hobby: ")
    except KeyboardInterrupt:
        return
    
    sq.add_student(name, age, hobby)
    
    

def _exit():
    return True

def main():
    sq.init_table()

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
