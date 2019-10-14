
todo_list = {1: {'task name': 'hangman', 'due date': '7-10-2019', 'status': 'finished', 'priority': 'important'},
             2: {'task name': 'login system', 'due date': '10-10-2019', 'status': 'finished', 'priority': 'important'}}

print("""This is a todo list application.
You can add tasks to the todo list.
You can set a due date to this task.
You can check a task completed or not.
You can set a priority for this task.
You can delete a task from the list""")


def add_task():
    task_name = input("Enter the task name :")
    due_date = input("Enter the due date as DD-MM-YYYY :")
    priority = input("Enter the priority as 'important or 'not important'")
    status = input("Enter the status as 'completed' or 'not completed'")
    todo_list[len(todo_list) + 1] = {'task name': task_name, 'due date': due_date, 'priority': priority,
                                     'status': status}
    print("The task is added to the list\n")
    show()

def task_update():
    task_no = input("Enter the number of the task you want to update : ")

    task_name = input("Enter the task name :")
    due_date = input("Enter the due date as DD-MM-YYYY :")
    priority = input("Enter the priority as 'important or 'not important'")
    status = input("Enter the status as 'completed' or 'not completed'")
    todo_list[int(task_no)] = {'task name': task_name, 'due date': due_date, 'priority': priority, 'status': status}
    print("The task is updated\n")
    show()
def task_delete():
    number = input("Enter the number of the task you want to delete : ")
    del todo_list[int(number)]
    print("The task is deleted\n")
    show()
def show():
    print("Existing tasks:\n")
    print("    Task Number        Name Of The Task       Due Date             Status            Priority")
    number=1
    for task_num, task_def in todo_list.items():
        name = task_def['task name']
        due = task_def['due date']
        stat = task_def['status']
        prio = task_def['priority']
        print(f"{number:^20}{name:^20}{due:^20}{stat:^20}{prio:^20}")
        number+=1

def greeting():
    show()
    while True:
        print("""
        1 for adding new task.
        2 for updating an existing task.
        3 for deleting an existing task.
        q for quit
        """)

        choise=input("ENTER YOUR CHOISE:\n")

        if choise=='1':
            add_task()
        elif choise=='2':
            task_update()
        elif choise=='3':
            task_delete()
        else:
            quit()


greeting()