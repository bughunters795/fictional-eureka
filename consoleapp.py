# todo-app console projects 
import os
tasks = []


#add feature :
if os.path.exists("file.txt"):
    with open("file.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
def add():

            while True:
                a = input("Enter your task's:\n")
                if(a== 'done' or a == 'exit' or a== 'clear' or a =='m'):
                    print('no task added')
                    break
                else:
                    tasks.append(a)
                    with open("file.txt", 'a') as file:
                        file.write(a+'\n')
                        print(f"Task added: {a}")


            
# show feature:

def show():
                if not tasks:
                    print("No tasks found.")
                else:
                    print("Your Tasks:")
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                print("\nOpening file.txt...\n")
                os.system('notepad file.txt')

# delete feature:
def delete():
    show()
    v = input("Which task number do you want to delete?\n")
    
    if v.isdigit():
        v = int(v)  
        if 1 <= v <= len(tasks):
             tasks.pop(v-1)
        with open("file.txt", "w") as file:
            for task in tasks:
                file.write(f"{task}\n")

    elif not tasks:
        print("No tasks to delete.")
        return
    else:
         print('no task is added ')
    
    show()

def menu():
    while True:
        print("[--------------------Todo-App-------------------------------]")
        print("Menu:")
        print("1. ADD")
        print("2. Show")
        print("3. Delete")
        print("4. Exit")
        print("[--------------------Todo-App-------------------------------]\n")
        choice = input("Enter your choice: ")


        if choice   == '1':
            add()
        elif choice == '2':
            show()
        elif choice == '3':
            delete()
        elif choice == '4':
            print("Thanks for using the app! Goodbye 👋")
            break
        else:
            print("Invalid choice. Please select from 1-4.")

menu()

