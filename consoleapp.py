# todo-app console projects 

#add feature :

def add():
    tasks = []
    while True:
            a = input("Enter your task's:\n")
            if(a== 'done' or a == 'exit' or a== 'clear'):
                print('no task added')
                print(tasks)
                break
            else:
                tasks.append(a)
                print(tasks)
                print('task added  ')

add()
print("thank's for comming ")



