# todo-app console projects 

#add feature :
tasks = []

def add():
    while True:
            a = input("Enter your task's:\n")
            if(a== 'done' or a == 'exit' or a== 'clear'):
                print('no task added')
                # print(tasks)
                show()
                break
            else:
                tasks.append(a)
                # print(tasks)
                # print('task added  ')
                # return tasks
                show()

def show():
        if(tasks == '' ):
              print("No tasks found.")
        else:
            print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

add()
print("thank's for comming ")