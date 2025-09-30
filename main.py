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
    
    menu.confirm_return(f"Added \"{name}\" to db. ")
    
def list_students():
    students = sq.get_all_students()

    if not students: 
        menu.confirm_return("No students in db. ")
        return

    format = "{:<15} {:<5} {:<15}"
    print(format.format("Name:", "Age:", "Hobby:"))

    for student in students:
        print(format.format(student[0], student[1], student[2]))

    menu.confirm_return()

def search_student():
    name_to_search = ""
    try:
        while not name_to_search:
            name_to_search = input("Search student by name: ")
    except KeyboardInterrupt:
        return

    found_students = sq.search_student(name_to_search)

    amount_found = 0
    if found_students:
        for student in found_students:
            print(f"Name: {student[0]}, Age: {student[1]} Hobby: {student[2]}")
            amount_found += 1

    if amount_found == 0:
        menu.confirm_return(f"No student with name {name_to_search}. ")
    else:
        menu.confirm_return(f"Found {amount_found} student/s with that name. ")

def calculate_avg_age():
    avg_age = sq.get_avg_age()

    if avg_age is None:
        menu.confirm_return("No students in db. ")
        return

    menu.confirm_return(f"The average age is {avg_age}. ")




def _exit():
    return True

def main():
    sq.open()
    sq.init_table()

    actions = {
        "Add student": add_student,
        "List all students": list_students,
        "Search student": search_student,
        "Calculate average age": calculate_avg_age,
        "Exit": _exit
    }

    while True:
        exit_loop = menu.select_action(actions)

        if exit_loop:
            break

    sq.close()

if __name__ == "__main__":
    main()
