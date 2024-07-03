todolist = []

def add_task(task):
    todolist.append(task)
    print("Task Successfully Added")

def view_task():
    if not todolist:
        print("No tasks found!")
    else:
        print("Tasks:")
        for index, item in enumerate(todolist, 1):
            print(f"No.{index} - {item}")
contact = {}
def add_contact(name,number):
    contact[name] = number
    print("Contact Added Succesfully!")

def view_contact():
    if not contact:
        print("Contact Not Found!")
    else:
        print("Contacts:- ")
        for Index, (name, number) in enumerate(contact.items(), 1):
            print(f"No.{Index} - Name: {name}, Number: {number}")
if __name__ == "__main__":
    while True:
        print("\nChoose An Option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Add Contact")
        print("4. View Contact")
        print("5. Exit")

        
        choice = int(input("Enter the Option: "))
        if choice == 1:
            task = input("Enter the Task: ")
            add_task(task)
        elif choice == 2:
            view_task()
        elif choice ==3:
            name = input("Enter The Name here:- ")
            number = int(input("Enter The Number here:- "))
            add_contact(name,number)
        elif choice == 4:
            view_contact()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Option! Please choose 1, 2, or 3.")

